# 🖼️ Image Segmentation Website

This is a Flask-based web application for image background removal using the U²-Net model. Users can upload an image, and the app returns a segmented version.

## 🚀 Features

- Upload images for segmentation.
- Perform background removal using U²-Net.
- Simple and user-friendly web interface.

## 📦 Project Structure

```
├── model_weights/        # Pre-trained U²-Net model weights
│   └── u2netp.pth        # U²-Net lightweight model
├── static/uploads/       # Uploaded images
├── templates/            # HTML templates for Flask pages
│   ├── upload.html       # Image upload form
│   └── display_image.html# Display segmented image
├── app.py                # Flask web application
├── main.py               # Image processing logic
├── data_loader.py        # Data loading utilities
├── u2net.py              # U²-Net model definition
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## ⚙️ Installation

1. **Clone the Repository:**
```bash
git clone https://github.com/yourusername/segmentation_website.git
cd segmentation_website
```

2. **Create Virtual Environment (Recommended):**
```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Ensure Model Weights:**
- Place `u2netp.pth` in the `model_weights` directory.
- Download from the [official U²-Net repository](https://github.com/xuebinqin/U-2-Net) if missing.

## 🖱️ Usage

1. **Run Flask App:**
```bash
python app.py
```

2. **Access Web App:**
Open [http://localhost:5000](http://localhost:5000) in your browser.

3. **Upload Image:**
- Choose an image.
- View the segmented output.

## 📊 Example Output

- **Input:** Uploaded image  
- **Output:** Segmented image with background removed.

## 📝 License

This project is open-source under the **MIT License**.  
See [MIT License](https://opensource.org/licenses/MIT) for details.

## 🤝 Contributing

Contributions are welcome! Submit a pull request or report issues.
