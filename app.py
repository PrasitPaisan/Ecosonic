import librosa
import shutil
import os
from PIL import Image
from tensorflow.keras.models import load_model

from service.redution import reduce_audio_noise
from service.cut_sound import cut_sound_per_action
from utils.plot_compare import plot_compare
from utils.convert_to_byte import convert_to_2bytes
from service.converting_sound_to_mel_image import sound_to_image
from utils.preprocess_the_image import convert_to_array
from sensor.open_lib_control import setup_GPIO_servo, set_angle
from sensor.stepper_controls import setup_gpio, motor_control
from sensor.IR_sensor import read_ir_sensor

Image.MAX_IMAGE_PIXELS = None

if __name__ == "__main__":
    try:
        input_path = "/home/visionhelper/Documents/data_for_test/test_random2.wav"
        class_names = ['battery', 'bottle', 'can', 'glass', 'paper', 'pingpong', 'plastic']
        model = load_model("./models/VGG16_pre_ep100_01_.h5")
        sample_rate = 22050
        while True:

            original_audio, sr = librosa.load(input_path, sr=sample_rate)
            reduced_audio, _sr = reduce_audio_noise(input_path, sample_rate)

            audio_segment = convert_to_2bytes(reduced_audio, _sr)

            # plot_compare(original_audio=original_audio, reduced_audio=reduced_audio, sample_rate=sr)

            cut_sound_per_action(audio_segment, "./results/sound", _sr)
        
            sound_to_image(dataset_path="./results/sound", output_path="./images", n_mels=128, n_fft=2048, hop_length=512)

            # Predict the image
            for dirpath, dirnames, filenames in os.walk("./images"):
                for f in filenames:
                    if f.endswith('.png'):
                        img_path = os.path.join(dirpath, f)
                        img_array = convert_to_array(img_path)
                        pred = model.predict(img_array)
                        predicted_class_index = pred.argmax(axis=1)[0]
                        print(f"Predicted class for {f} : {class_names[predicted_class_index]}")
            

            # Detete the results after finish prediction
            shutil.rmtree('./results')
            shutil.rmtree("./images")

    except KeyboardInterrupt:
        print("Exiting program")
        pwm.stop()
	    GPIO.cleanup()