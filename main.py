# main.py
import os
import glob
import numpy as np
import torch
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torchvision import transforms
from skimage import io
from PIL import Image
from data_loader import RescaleT, ToTensorLab, SalObjDataset
from u2net import U2NETP  # Ensure U2NETP is in the same directory or properly imported

def normPRED(d):
    ma = torch.max(d)
    mi = torch.min(d)
    dn = (d - mi) / (ma - mi)
    return dn

def save_output(image_name, pred, d_dir):
    predict = pred.squeeze()
    predict_np = predict.cpu().data.numpy()
    im = Image.fromarray((predict_np * 255).astype(np.uint8)).convert('RGB')
    
    # Read the original image
    image = io.imread(image_name)
    imo = im.resize((image.shape[1], image.shape[0]), resample=Image.BILINEAR)
    pb_np = np.array(imo)

    img_name = os.path.basename(image_name).split(".")[0]
    imo.save(os.path.join(d_dir, img_name + '_processed.png'))

def process_image(image_path):
    model_name = 'u2netp'  # or 'u2net' if you want the larger model
    model_dir = "model_weights/u2netp.pth"  # Adjust the path if necessary
    prediction_dir = 'static/uploads'

    # Prepare the dataset
    img_name_list = [image_path]
    test_salobj_dataset = SalObjDataset(
        img_name_list=img_name_list,
        lbl_name_list=[],
        transform=transforms.Compose([RescaleT(320), ToTensorLab(flag=0)])
    )
    test_salobj_dataloader = DataLoader(test_salobj_dataset, batch_size=1, shuffle=False, num_workers=1)

    # Load the model
    net = U2NETP(3, 1)
    net.load_state_dict(torch.load(model_dir, map_location='cpu', weights_only=True))
    net.eval()

    # Inference
    for i_test, data_test in enumerate(test_salobj_dataloader):
        inputs_test = data_test['image'].type(torch.FloatTensor)
        inputs_test = Variable(inputs_test)

        d1, _, _, _, _, _, _ = net(inputs_test)  # Get the output from the model
        pred = d1[:, 0, :, :]  # Take the first output layer
        pred = normPRED(pred)  # Normalize the prediction

        # Save the processed image
        if not os.path.exists(prediction_dir):
            os.makedirs(prediction_dir, exist_ok=True)
        save_output(image_path, pred, prediction_dir)

    img_name = os.path.basename(image_path).split(".")[0]
    processed_image_name = f"{img_name}_processed.png"
    
    # Save the processed image
    if not os.path.exists(prediction_dir):
        os.makedirs(prediction_dir, exist_ok=True)
    save_output(image_path, pred, prediction_dir)

    return processed_image_name  # Return just the filename

    # return os.path.join(prediction_dir, os.path.basename(image_path).split(".")[0] + '_processed.png')
