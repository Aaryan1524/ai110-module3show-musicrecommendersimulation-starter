# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**  

---

## 2. Intended Use  

The system is designed to suggest top 3 to 5 songs from a small local CSV catalog based on a user's stated preference for genre, mood, and energy level. It assumes that users have a singular defined taste at any given moment and that users explicitly identify their preferences. It is specifically for classroom exploration rather than large-scale deployment.

---

## 3. How the Model Works  

VibeFinder 1.0 evaluates every song in its database against the user's provided profile preferences. It checks three features:
- **Genre Match:** Awards (+2.0) points if the track's genre is identical to the user's favorite genre.
- **Mood Match:** Awards (+1.0) points for matching the user's mood.
- **Energy Match:** Awards up to (+1.0) points based on how closely the track's energy scale (0.0 to 1.0) matches the target. It subtracts points when the song's energy level is further away from the user's intent.
The final scores are summed up, and the top choices are sorted descending to generate recommendations. I expanded the dataset and refined energy scoring to penalize large energy discrepancies.

---

## 4. Data  

The dataset is a custom `songs.csv` catalog containing exactly 15 songs. It covers several distinct genres like pop, lofi, rock, jazz, edm, and classical. The original 10-song dataset was expanded with 5 additional hand-crafted songs to improve diversity in acoustic/folk and classical choices. However, huge sections of modern and international musical genres are missing, heavily skewing representations to Western pop/rock tastes.

---

## 5. Strengths  

VibeFinder works very well at grouping obvious mood profiles like "Chill Lofi", perfectly mapping chill vibe preferences to its 2 or 3 lofi tracks with scoring clarity. It excels in explicit targeting, providing clear, transparent explainability (e.g., "Because: genre match (+2.0)") which many black-box AI platforms fail to offer users.

---

## 6. Limitations and Bias 

The most apparent bias is the "genre trap". Because genre is weighted twice as much as any other feature, the system aggressively prioritizes a pop song with wrong energy/mood over a rock song that perfectly matches the user's energy and mood. This creates filter bubbles by trapping the user inside one style. Secondly, because the catalog contains almost ~40% electronic/synth/lofi, users with those tastes get significantly better suggestions than classical/jazz fans. The scoring rigidly enforces exact string matches for genres, isolating closely-related subgenres unfairly.

---

## 7. Evaluation  

I tested four profiles: `High-Energy Pop`, `Chill Lofi`, `Deep Intense Rock`, and an adversarial `Adversarial Edge Case` (Classical/Intense/0.95 Energy). 
- In the `Chill Lofi` context, recommendations cleanly favored low-energy, chill tracks, performing intuitively.
- **Surprises:** In the `Adversarial Edge Case`, someone looking for "Intense Classical" found "Sad Piano" as its top choice, only because it had the exact "classical" string match, but it severely failed in satisfying the *Intense* or *0.95 energy* preference. Similarly, an EDM track ranked second only because of matching energy.
- **Reflection on Differences:** Comparing "Deep Intense Rock" vs "Adversarial Edge Case", both asked for 0.95 energy, but the Rock profile found a perfect match. The adversarial profile failed because the dataset literally lacked high-energy classical tracks. This proves the system is extremely fragile to dataset gaps.

---

## 8. Future Work  

If I kept developing this, I would:
- Change the strict genre matching to "Genre Proximity" (e.g., accepting Jazz matches as similar to Blues) to boost diversity.
- Introduce a "Diversity Penalty" that downranks subsequent songs from the identical artist or genre to prevent repetitive Top 3 results.
- Implement soft-matching for textual tags (using semantic embeddings for mood) instead of exact string checks.

---

## 9. Personal Reflection  

Building this small recommender helped me realize how basic math loops can occasionally "feel" intelligent just by surfacing matching tokens. I was surprised at how heavily the system mirrored the biases present in the tiny 15-song dataset; the system physically couldn't satisfy an intense-classical user because no such song existed. It made me realize that in real-world platforms like Spotify, human/editorial curation and dataset audits are necessary precisely because basic recommendation algorithms only blindly score what already exists. They don't know when they're giving you a bad song; they just pick the mathematically "least bad" one.
