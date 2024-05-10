# Phishing Detector

![Phishing Detector Banner](images/Image-Banner_1.png)

Phishing Detector is a web application developed with Streamlit that uses predefined rules to analyze text and determine if it contains phishing indicators.

## Features

- Allows uploading text files or entering text manually for analysis.
- Automatically detects the language of the text and applies specific rules for that language (currently supports only English and Spanish).
- Displays a list of detected phishing rules and the probability of the text being a phishing attempt.
- Allows adjusting the probability threshold for classifying text as phishing.
- Provides a user-friendly interface with Streamlit.

## Installation

1. Clone this repository:

    ```bash
    git clone <https://github.com/your_username/phishing-detector.git>
    ```

2. Install dependecies:

    ```bash
    cd phishing-detector
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    streamlit run app.py
    ```

2. In the user interface, upload a text file or enter text manually in the text area.
3. Select the phishing rules you want to evaluate and adjust the probability threshold if necessary.
4. Click the "Analyze" button to start the analysis.
5. Observe the results in the user interface and the console.

## Contribution

Contributions are welcome! If you want to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: git checkout -b feature/new-feature or git checkout -b bugfix/fix-bug.
3. Make your changes and commit with descriptive messages: git commit -m "Detailed explanation of the changes".
4. Push your branch to your remote repository: git push origin feature/new-feature.
5. Open a pull request in the original repository and describe your changes in detail.

## Credits

Developed by Lázaro Bustio-Martínez, PhD. and Vitali Herrera-Semenets, PhD.

## License

This project is licensed under the MIT License.
