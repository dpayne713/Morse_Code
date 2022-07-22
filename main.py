from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from morse import MorseCodeLogic
import audio
from scipy.io.wavfile import write

audio_files = audio.Audio()
morse_logic = MorseCodeLogic()

morse_string = None

def convert():
    """
    Activates the conversion functionality
    no return value
    """
    global morse_string
    # Get user text input
    text_input = txt_area.get("1.0", 'end')
    # check Radio button choice (To Morse or From Morse)
    if to_morse.get():
        # convert text to morse code string and turn on save .wav button
        return_string = morse_logic.to_morse(text_input)
        morse_string = return_string
        save_btn.grid(column=0, row=4)
    else:
        # convert morse string to readable text
        return_string = morse_logic.from_morse(text_input)
        save_btn.destroy()
    # Clear output text area and display newly computed text
    output_txt_area.delete('1.0', 'end')
    output_txt_area.insert("1.0", return_string)


def save_file(morse_str):
    """ Saves a .wav file to user selected location
    function uses audio_files.write_sine_wave method.
    No return value."""
    data = audio_files.write_sine_wave_file(morse_str)
    f_path = filedialog.asksaveasfile(defaultextension='.wav', initialfile="morse_code.wav").name
    write(f_path, data['sample_rate'], data['data'])

# tkinter base window
root = Tk()
root.minsize(width=600, height=400)

# Frame for input areas
content = Frame(root, padding=30)
content.grid(column=0, row=0)
root.title("Morse Code Converter")
input_label = Label(content, text="Input text or morse code: ").grid(column=0, row=1)
input_text = StringVar()
txt_area = Text(content, width=50, height=20)
txt_area.grid(column=0, row=2)
output_txt_area_label = Label(content, text="Output: ").grid(column=0, row=3)
output_txt_area = Text(content, width=50, height=20 )
output_txt_area.grid(column=0, row=4)

#Frame for interactable elements
btn_frame = Frame(content, padding=40)
btn_frame.grid(column=1, row=0, rowspan=5)
to_morse = BooleanVar(None, True)
text_to_morse = Radiobutton(btn_frame, text="Text to Morse", variable=to_morse, value=True)
text_to_morse.grid(column=0, row=0)
morse_to_text = Radiobutton(btn_frame, text="Morse to Text", variable=to_morse, value=False)
morse_to_text.grid(column=0, row=1)
convert_btn = Button(btn_frame, text='Convert', command=convert)
convert_btn.grid(column=0, row=2)
save_btn = Button(btn_frame, text='Save as .wav', command=lambda: save_file(morse_string))


if __name__ == '__main__':
    root.mainloop()
