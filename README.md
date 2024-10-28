# **SynthDog-RTL**

SynthDog-RTL is a specialized tool for generating synthetic datasets tailored for RTL (Right-to-Left) languages such as **Arabic, Urdu, Persian, Hebrew, Hindi**, and other similar languages. This repository is based on the original SynthDog designed for LTR (Left-to-Right) languages, and includes modifications to support RTL text rendering for OCR applications, particularly using the **Donut OCR** model.

## **Overview**

SynthDog-RTL enables Machine Learning Engineers to create synthetic datasets that are crucial for training OCR models for RTL languages. This is especially useful for document analysis tasks, data extraction, and multilingual document processing using Donut OCR or similar models.

### **Key Features**:
- Full support for RTL languages.
- Configurable synthetic data generation.
- Adjustable parameters for dataset quality, layout, and image effects.
- Capability to incorporate custom fonts and language-specific text corpora.

## **Installation**

To get started, first, clone this repository and install the required dependencies:

```bash
git clone https://github.com/aiviewz/Synthdog-RTL.git
cd Synthdog-RTL
pip install synthtiger Pillow==9.5.0
```

## **Project Structure**

```
/Synthdog-RTL
  ├── resources/
  │   ├── background/
  │   ├── paper/
  │   ├── font/
  │   │   └── ur/         # Folder for Urdu fonts
  │   └── corpus/
  │       └── urdu_sample.txt  # Sample text for Urdu
  └── config_ur.yaml       # Configuration file for Urdu
```

### **Explanation**:
- **background/**: Background images for the synthetic documents.
- **paper/**: Paper texture images.
- **font/**: Font files for target RTL languages.
- **corpus/**: Sample text for target languages.

## **Usage**

To generate synthetic datasets, follow these steps:

### **Step 1: Setup Configuration**

1. Create a text file (`urdu_sample.txt`) with sample paragraphs in your target language (e.g., Urdu).
   
2. Download fonts from **Google Fonts** that support your language and place them in the appropriate directory under `resources/font/`.

   For instructions on downloading fonts from Google Fonts, check the [Google Fonts Documentation](https://fonts.google.com/).

3. Modify the configuration file (e.g., `config_ur.yaml`) to specify language-specific settings, font paths, and corpus paths.

### **Step 2: Generate Dataset**

Run the following command to generate the dataset:

```bash
synthtiger -o ./outputs/SynthDoG_ur -c 10 -w 2 -v template.py SynthDoG config_ur.yaml
```

#### **Parameters**:
- `-o`: Output directory for generated images.
- `-c`: Number of samples to generate.
- `-w`: Number of workers to use.
- `config_ur.yaml`: Configuration file with dataset settings.

For more detailed instructions on generating datasets and customizing configurations, check the [Complete Tutorial](#).

## **Customization Guide**

Below are some common attributes you might want to adjust in the configuration file (`config_ur.yaml`) for customization:

- **Document Layout**:
  - `landscape`: Adjust to `1` for landscape orientation or `0` for portrait.
  - `fullscreen`: Set to `1` to fill the entire document background with text.

- **Text Adjustments**:
  - `font.bold`: Set to `1` to enable bold text.
  - `align`: Modify alignment (e.g., `right` for RTL languages).

- **Effects**:
  - Elastic distortion, noise, and blur parameters can be adjusted for creating more diverse synthetic datasets.

## **Adding New Languages**

To extend support for other RTL languages, follow these steps:
1. Create a new corpus file with sample text in the target language.
2. Add relevant fonts to the `resources/font/<language-code>/` directory.
3. Update the configuration file paths to reflect the new language resources.

## **References & Acknowledgments**

This repository is based on the original [SynthDoG for LTR Languages](https://github.com/clovaai/donut/tree/master/synthdog) developed by Clova AI. Any copyright-related queries should refer to the original repository.

For additional information on using SynthDog-RTL and customizing configurations, see our [Complete Tutorial](#).

## **License**

Refer to the [LICENSE](LICENSE) file for detailed license information.

## **Contributions**

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions for improvement or new features.

---

This `README.md` provides a comprehensive introduction and guide to using SynthDog-RTL, along with references to the original SynthDog for any copyright considerations.
