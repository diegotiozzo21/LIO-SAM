import numpy as np
import matplotlib.pyplot as plt

def read_matrices_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    gnss_start = lines.index("GNSSPathMatrixENU\n") + 1
    lio_start = lines.index("LIOPathMatrix\n") + 1

    gnss_lines = lines[gnss_start:lio_start - 1]
    lio_lines = lines[lio_start:]

    GNSSPathMatrixENU = np.array([list(map(float, line.split())) for line in gnss_lines])
    LIOPathMatrix = np.array([list(map(float, line.split())) for line in lio_lines])

    return GNSSPathMatrixENU, LIOPathMatrix

def plot_paths(GNSSPathMatrixENU, LIOPathMatrix):
    plt.figure()
    plt.plot(GNSSPathMatrixENU[0, :], GNSSPathMatrixENU[1, :], label='GNSS Path')
    plt.plot(LIOPathMatrix[0, :], LIOPathMatrix[1, :], label='LIO Path')
    plt.xlabel('East (m)')
    plt.ylabel('North (m)')
    plt.legend()
    plt.title('Paths')
    plt.show()

def path_length(path):
    return np.sum(np.linalg.norm(path[:, 1:] - path[:, :-1], axis=0))

if __name__ == "__main__":
    GNSSPathMatrixENU, LIOPathMatrix = read_matrices_from_file('paths.txt')
    plot_paths(GNSSPathMatrixENU, LIOPathMatrix)
    print(f"GNSS path length: {path_length(GNSSPathMatrixENU)}")
    print(f"LIO path length: {path_length(LIOPathMatrix)}")