import numpy as np

if __name__ == '__main__':
    n = 20
    m = 10000
    # construct vector of n random numbers with zero mean and unit variance
    x = np.random.randn(n)  # shape (n,)

    # draw with replacement from x n times
    x_drawings = np.random.choice(x, size=(n, m))  # shape (n, m)

    # compute the sample mean for each drawing
    x_mean = np.mean(x_drawings, axis=0)  # shape (m,)

    # compute the standard deviation of the sample means
    avg_perf_1 = np.mean(x_mean)  # shape (1,)
    stddev_1 = np.std(x_mean)  # shape (1,)
    stddev_1_2 = np.sqrt(np.sum((x_mean - avg_perf_1)**2/m))  # shape (1,) # same as stddev_1
    stderr_1 = stddev_1

    avg_perf_2 = np.mean(x_mean)  # shape (1,)
    stddev_2 = np.sqrt(np.sum((x_mean - avg_perf_2)**2/n))  # shape (1,)
    stderr_2 = stddev_2 / np.sqrt(n - 1)

    avg_perf_3 = np.mean(x_mean)  # shape (1,)
    stddev_3 = np.sqrt(np.sum((x_mean - avg_perf_3)**2/m))  # shape (1,)
    stderr_3 = stddev_3 / np.sqrt(n - 1)

    stderr_of_the_mean = 1 / np.sqrt(n)  # 1 is std of the base distribution
    stderr_of_the_mean_2 = np.std(x) / np.sqrt(n - 1)
    stderr_of_the_mean_w = np.std(x) / np.sqrt(n)

    stddev_x = np.std(x)  # shape (1,)
    stddev_rost = np.sqrt(np.sum((x - np.mean(x))**2)/n)
    stderr_rost = stddev_rost / np.sqrt(n - 1)

    y = np.random.randn(n, m)  # shape (n,m)
    y_mean = np.mean(y, axis=0)  # shape (m,)

    # count how many in y_mean are within stderr_1 from base distribution
    count_1 = np.sum(np.abs(y_mean - 0) < stderr_1)
    perc_1 = count_1 / m

    # count how many in y_mean are within stderr_2 of avg_perf_2
    count_2 = np.sum(np.abs(y_mean - 0) < stderr_2)
    perc_2 = count_2 / m

    # count how many in y_mean are within stderr_of_the_mean of avg_perf_2
    count_3 = np.sum(np.abs(y_mean - 0) < stderr_of_the_mean)
    perc_3 = count_3 / m

    # count how many in y_mean are within stderr_rost of avg_perf_2
    count_4 = np.sum(np.abs(y_mean - 0) < stderr_rost)
    perc_4 = count_4 / m

    count_5 = np.sum(np.abs(y_mean - 0) < stderr_3)
    perc_5 = count_5 / m
    print("Here we are now, entertain us")

