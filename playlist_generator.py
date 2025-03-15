import networkx as nx
import itertools

def create_transition_graph(tracks, bpm_weight=1, key_weight=1, energy_weight=1):
    """Creates a graph of tracks based on BPM, key, and energy compatibility with custom weighting."""
    G = nx.Graph()

    for t1, t2 in itertools.combinations(tracks, 2):
        bpm_diff = abs(t1["bpm"] - t2["bpm"])  # Minimize BPM jumps
        key_match = abs(t1["key"] - t2["key"]) in [0, 1]  # Favor harmonic mixing
        energy_diff = abs(t1["energy"] - t2["energy"])  # Avoid sudden energy jumps

        # Custom Weight Calculation
        weight = (
            (bpm_diff * bpm_weight) + 
            (0 if key_match else key_weight * 5) +  # Lower weight if keys match
            (energy_diff * energy_weight * 10)      # Energy scaled higher to balance impact
        )

        G.add_edge(t1["filename"], t2["filename"], weight=weight)

    # Use greedy TSP algorithm to find the best track order
    return nx.approximation.greedy_tsp(G)

# Example usage
if __name__ == "__main__":
    test_tracks = [
        {"filename": "song1.mp3", "bpm": 120, "key": 5, "energy": 0.7},
        {"filename": "song2.mp3", "bpm": 125, "key": 6, "energy": 0.4},
        {"filename": "song3.mp3", "bpm": 118, "key": 5, "energy": 0.9},
        {"filename": "song4.mp3", "bpm": 130, "key": 8, "energy": 0.8},
    ]

    # Customize weights (e.g., focus more on BPM and Key)
    bpm_weight = 2
    key_weight = 3
    energy_weight = 1

    ordered_filenames = create_transition_graph(test_tracks, bpm_weight, key_weight, energy_weight)
    print(ordered_filenames)
