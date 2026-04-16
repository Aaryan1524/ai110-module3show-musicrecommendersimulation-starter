"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.3},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
        "Adversarial Edge Case": {"genre": "classical", "mood": "intense", "energy": 0.95}
    }

    for name, prefs in profiles.items():
        print(f"\n--- Testing Profile: {name} ---")
        print(f"Preferences: {prefs}")
        recommendations = recommend_songs(prefs, songs, k=3)
        print("Top 3 recommendations:\n")
        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}\n")


if __name__ == "__main__":
    main()
