# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:49:02 2015

@author: maoter.chen
"""

"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster


######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.

    Return: tuple of closest pair.
    """

    dmin = float('inf')
    scpair = (dmin, -1, -1)
    for idx1 in range(len(cluster_list) - 1):
        for idx2 in range(idx1 + 1, len(cluster_list)):
            dist = pair_distance(cluster_list, idx1, idx2)
            if dist[0] < dmin:
                dmin = dist[0]
                scpair = (dist[0], idx1, idx2)
    return scpair


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    fcpair = (0, -1, -1)

    dummy_list = []
    if len(cluster_list) <= 3:
        for idx in range(len(cluster_list)):
            dummy_list.append(cluster_list[idx])
            fcpair = slow_closest_pair(dummy_list)
    else:
        mean = len(cluster_list) / 2
        cltr_left = cluster_list[:mean]
        cltr_right = cluster_list[mean:]
        # print "cltr_left=", cltr_left
        # print "cltr_right=", cltr_right
        fcpair_left = fast_closest_pair(cltr_left)
        fcpair_right = fast_closest_pair(cltr_right)
        # print "fcpair_left", fcpair_left
        # print "fcpair_right", fcpair_right
        if list(fcpair_left)[0] <= list(fcpair_right)[0]:
            fcpair = fcpair_left
        else:
            fcpair = (fcpair_right[0], fcpair_right[1] + mean, fcpair_right[2] + mean)

        mid = 0.5 * (cluster_list[mean - 1].horiz_center() + cluster_list[mean].horiz_center())
        pair_stp = closest_pair_strip(cluster_list, mid, list(fcpair)[0])
        if list(fcpair)[0] > list(pair_stp)[0]:
            fcpair = pair_stp
    return fcpair


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.
    """

    din_index = [index for index in range(len(cluster_list)) if
                 abs(cluster_list[index].horiz_center() - horiz_center) < half_width]
    din_list = []
    # print S_index
    for item in din_index:
        din_list.append(cluster_list[item])

    din_list.sort(key=lambda cluster: cluster.vert_center())
    # print "S_list", S_list
    dmin = float('inf')
    clpair = (dmin, -1, -1)
    # for idx1 in range(len(S_index)-2):
    for idx1 in range(len(din_index)):

        for idx2 in range(idx1 + 1, min(idx1 + 4, len(din_index))):

            dist = pair_distance(din_list, idx1, idx2)

            if dist[0] < dmin:
                dmin = dist[0]
                idxa = min(cluster_list.index(din_list[idx1]), cluster_list.index(din_list[idx2]))
                idxb = max(cluster_list.index(din_list[idx1]), cluster_list.index(din_list[idx2]))
                clpair = (dist[0], idxa, idxb)

    # print "cluster_list", cluster_list
    # print "S_index", S_index
    return clpair


# print "-------------"
# print fast_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 4, 0, 1, 0)])
# test2 =  fast_closest_pair([alg_cluster.Cluster(set([]), 0.32, 0.16, 1, 0), alg_cluster.Cluster(set([]), 0.39, 0.4, 1, 0), alg_cluster.Cluster(set([]), 0.54, 0.8, 1, 0), alg_cluster.Cluster(set([]), 0.61, 0.8, 1, 0), alg_cluster.Cluster(set([]), 0.76, 0.94, 1, 0)])
# print "test2", test2
# print "-------------"

# print closest_pair_strip([alg_cluster.Cluster(set([]), 0, 5, 1, 0), alg_cluster.Cluster(set([]), 1, 4, 1, 0), alg_cluster.Cluster(set([]), 2, 3, 1, 0), alg_cluster.Cluster(set([]), 3, 2, 1, 0)], 1.5, 3.0)
# print closest_pair_strip([alg_cluster.Cluster(set([]), -4.0, 0.0, 1, 0), alg_cluster.Cluster(set([]), 0.0, -1.0, 1, 0), alg_cluster.Cluster(set([]), 0.0, 1.0, 1, 0), alg_cluster.Cluster(set([]), 4.0, 0.0, 1, 0)], 0.0, 4.19)
# alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)]
# expected one of the tuples in set([(1.0, 1, 2)]) but received () (Exception: Length Error) When comparing against (1.0, 1, 2) (3 elements), the value, () (0 elements), has too few elements.

######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function mutates cluster_list
    Input: List of clusters, number of clusters
    Output: List of clusters whose length is num_clusters
    """
    # cp_cluster_list = []
    # cp_cluster_list = [list(elem) for elem in cluster_list]
    cp_cluster_list = [alg_cluster.Cluster(set([]), 0, 0, 0, 0) for dummy_index in range(len(cluster_list))]
    for idx in range(len(cluster_list)):
        cp_cluster_list[idx] = cluster_list[idx].copy()

    while len(cp_cluster_list) > num_clusters:
        cp_cluster_list.sort(key=lambda cluster: cluster.horiz_center())

        dummy_dist, node1, node2 = fast_closest_pair(cp_cluster_list)
        cp_cluster_list[node1].merge_clusters(cp_cluster_list[node2])
        del cp_cluster_list[node2]

    return cp_cluster_list


# a = alg_cluster.Cluster(set(['1']), 0, 0, 1, 0).merge_clusters(alg_cluster.Cluster(set(['1']), 0, 2, 1, 0))
# a.merge_clusters(alg_cluster.Cluster(set(['1']), 0, 4, 1, 0))
# print a
##print "-------------"
##print "hierarchical_clustering"
# cluster_list= [alg_cluster.Cluster(set(['01073']), 704.191210749, 411.014665198, 662047, 7.3e-05), alg_cluster.Cluster(set(['06059']), 113.997715586, 368.503452566, 2846289, 9.8e-05), alg_cluster.Cluster(set(['06037']), 105.369854549, 359.050126004, 9519338, 0.00011), alg_cluster.Cluster(set(['06029']), 103.787886113, 326.006585349, 661645, 9.7e-05), alg_cluster.Cluster(set(['06071']), 148.402461892, 350.061039619, 1709434, 7.7e-05)]
# print hierarchical_clustering(cluster_list, 2)
# print "cluster_list", cluster_list
# print cluster_list
# data = [2, set([('01073', '11001', '24510', '34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081', '51013', '51760', '51840', '54009', '55079'), ('06029', '06037', '06059', '06071', '06075', '08031', '41051', '41067')])]
##cluster_list= [alg_cluster.Cluster(set(['01073']), 704.191210749, 411.014665198, 662047, 7.3e-05), alg_cluster.Cluster(set(['06059']), 113.997715586, 368.503452566, 2846289, 9.8e-05), alg_cluster.Cluster(set(['06037']), 105.369854549, 359.050126004, 9519338, 0.00011), alg_cluster.Cluster(set(['06029']), 103.787886113, 326.006585349, 661645, 9.7e-05), alg_cluster.Cluster(set(['06071']), 148.402461892, 350.061039619, 1709434, 7.7e-05), alg_cluster.Cluster(set(['06075']), 52.7404001225, 254.517429395, 776733, 8.4e-05), alg_cluster.Cluster(set(['08031']), 371.038986573, 266.847932979, 554636, 7.9e-05), alg_cluster.Cluster(set(['24510']), 872.946822486, 249.834427518, 651154, 7.4e-05), alg_cluster.Cluster(set(['34013']), 906.236730753, 206.977429459, 793633, 7.1e-05), alg_cluster.Cluster(set(['34039']), 905.587082153, 210.045085725, 522541, 7.3e-05), alg_cluster.Cluster(set(['34017']), 909.08042421, 207.462937763, 608975, 9.1e-05), alg_cluster.Cluster(set(['36061']), 911.072622034, 205.783086757, 1537195, 0.00015), alg_cluster.Cluster(set(['36005']), 912.315497328, 203.674106811, 1332650, 0.00011), alg_cluster.Cluster(set(['36047']), 911.595580089, 208.928374072, 2465326, 9.8e-05), alg_cluster.Cluster(set(['36059']), 917.384980291, 205.43647538, 1334544, 7.6e-05), alg_cluster.Cluster(set(['36081']), 913.462051588, 207.615750359, 2229379, 8.9e-05), alg_cluster.Cluster(set(['41051']), 103.293707198, 79.5194104381, 660486, 9.3e-05), alg_cluster.Cluster(set(['41067']), 92.2254623376, 76.2593957841, 445342, 7.3e-05), alg_cluster.Cluster(set(['51013']), 865.681962839, 261.222875114, 189453, 7.7e-05), alg_cluster.Cluster(set(['51840']), 845.843602685, 258.214178983, 23585, 7.1e-05), alg_cluster.Cluster(set(['51760']), 865.424050159, 293.735963553, 197790, 8.6e-05), alg_cluster.Cluster(set(['55079']), 664.855000617, 192.484141264, 940164, 7.4e-05), alg_cluster.Cluster(set(['54009']), 799.221537984, 240.153315109, 25447, 7.7e-05), alg_cluster.Cluster(set(['11001']), 867.470401202, 260.460974222, 572059, 7.7e-05)]
# cluster_list= [alg_cluster.Cluster(set(['01073']), 704.191210749, 411.014665198, 662047, 7.3e-05), alg_cluster.Cluster(set(['06059']), 113.997715586, 368.503452566, 2846289, 9.8e-05), alg_cluster.Cluster(set(['06037']), 105.369854549, 359.050126004, 9519338, 0.00011), alg_cluster.Cluster(set(['06029']), 103.787886113, 326.006585349, 661645, 9.7e-05), alg_cluster.Cluster(set(['06071']), 148.402461892, 350.061039619, 1709434, 7.7e-05)]
##print hierarchical_clustering(cluster_list, 2)
# print "cluster_list", cluster_list
######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function mutates cluster_list

    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """
    # print "cluster_list1", cluster_list
    cp_cluster_list = cluster_list[:]
    cp_cluster_list.sort(key=lambda cluster: cluster.total_population())
    cp_cluster_list.reverse()
    # print "cluster_list", cluster_list

    centers = cp_cluster_list[:num_clusters]
    # print "centers=", centers

    for dummy_idx in range(num_iterations):
        new_clusters = [alg_cluster.Cluster(set([]), 0, 0, 0, 0) for dummy_index in range(num_clusters)]
        for cluster in cp_cluster_list:
            dmin = float('inf')
            center_idx = 0
            for center in centers:
                # print "cluster", cluster
                # print "center", center
                dist = cluster.distance(center)
                # print dist
                if dist < dmin:
                    dmin = dist
                    center_idx = centers.index(center)
            new_clusters[center_idx].merge_clusters(cluster)

        for idx1 in range(num_clusters):
            centers[idx1] = new_clusters[idx1]

    # position initial clusters at the location of clusters with largest populations
    # print "cluster_list1", new_clusters
    # print "cluster_list2", cluster_list
    return new_clusters
print "-------------"
print "kmeans_clustering"
cluster_list= [alg_cluster.Cluster(set(['01073']), 704.191210749, 411.014665198, 662047, 7.3e-05), alg_cluster.Cluster(set(['06059']), 113.997715586, 368.503452566, 2846289, 9.8e-05), alg_cluster.Cluster(set(['06037']), 105.369854549, 359.050126004, 9519338, 0.00011), alg_cluster.Cluster(set(['06029']), 103.787886113, 326.006585349, 661645, 9.7e-05), alg_cluster.Cluster(set(['06071']), 148.402461892, 350.061039619, 1709434, 7.7e-05)]
print kmeans_clustering(cluster_list, 2, 2)
print cluster_list

