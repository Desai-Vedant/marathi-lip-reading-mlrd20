# Marathi Lip Reading Dataset (MLRD-20)

**MLRD-20** is a word-level lip reading dataset in the Marathi language, created by recording videos from 38 native speakers. The dataset contains isolated word utterances, mouth-cropped videos, and associated annotations. This repository provides the annotation files, sample videos, and processing/training code for researchers and developers working on visual speech recognition in low-resource languages.

---

## 📦 Dataset Overview

- **Language:** Marathi
- **Total Speakers:** 38
- **Vocabulary Size:** 20 words
- **Total Videos (Original):** 760
- **With Augmentation (lighten/darken):** 2,280 videos
- **Video Format:** `.mp4`, 64x64 pixels, 2 seconds, 25 FPS
- **Augmentations:** Lighten, Darken (x3 total per word)

---

## 🗂 Directory Structure

```
marathi-lip-reading-mlrd20/
├── annotation.csv               # CSV file with word ID and label
├── notebooks/
│   └── mlrd20_demo.ipynb        # Sample notebook for loading and using the dataset
├── scripts/
│   ├── preprocess.py            # OpenCV-based preprocessing (e.g., mouth ROI)
│   └── augment.py               # Code for video augmentation
├── LICENSE                      # MIT License (for code)
├── LICENSE-CC-BY-SA-4.0         # CC BY-SA 4.0 (for dataset)
└── README.md
```

---

## 🧾 Annotations

The `annotation.csv` file contains mappings of video filenames to their corresponding words:

| Filename             | Word ID | Word (Marathi)   |
|----------------------|---------|------------------|
| s1_w1_lighten.mp4    | w1      | छत्रपती          |
| s2_w2_darken.mp4     | w2      | शिवाजी           |
| ...                  | ...     | ...              |

---

## 🗣 Vocabulary (20 Words)

```
w1: छत्रपती       w11: महान
w2: शिवाजी        w12: राजे
w3: महाराज        w13: होते
w4: हे             w14: त्यांनी
w5: महाराष्ट्राच्या w15: रयतेचे
w6: मातीमध्ये      w16: राज्य
w7: जन्मलेले       w17: म्हणजेच
w8: एक             w18: स्वराज्य
w9: शूरवीर         w19: स्थापना
w10: आणि           w20: केले
```

---

## 🚀 How to Use

1. Download the full dataset from [Kaggle](https://www.kaggle.com/your-dataset-link).
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/marathi-lip-reading-mlrd20.git
   cd marathi-lip-reading-mlrd20
   ```
3. Open the `notebooks/mlrd20_demo.ipynb` to view a working example of how to load and process videos and annotations.

---

## 🧠 Model

We tested this dataset using a 3DCNN + BLSTM architecture for lip reading. The training and evaluation code will be added in the future.

---

## 👨‍💻 Authors

This dataset and repository were created by:

- **Vedant Desai** — Processing using OpenCV and structuring  
- **Muaaj Nesarikar** — Processing using OpenCV and structuring  
- **Aditya Patil** — Recording and documentation  
- **Sushant More** — Recording and documentation  

---

## 📄 License

- 🧠 **Code** is licensed under the [MIT License](LICENSE).
- 📊 **Dataset** (videos + annotations) is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

---

## 📬 Citation

To cite this dataset in your research, please use the following BibTeX (example):

```bibtex
@misc{mlrd2025,
  title={MLRD-20: A Marathi Lip Reading Dataset},
  author={Vedant Desai and Muaaj Nesarikar and Aditya Patil and Sushant More},
  year={2025},
  note={https://www.kaggle.com/your-dataset-link}
}
```

---

## 🙌 Acknowledgements

Special thanks to all student volunteers who contributed recordings for this dataset.
