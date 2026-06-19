"""Check if microphone device is accessible."""
import pyaudio

print("Checking audio devices...\n")

p = pyaudio.PyAudio()
default_input = p.get_default_input_device_info()
default_idx = default_input['index']

print(f"Total audio devices: {p.get_device_count()}\n")

for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    is_input = info['maxInputChannels'] > 0
    is_default = (i == default_idx)
    
    if is_input:
        print(f"Device {i}: {info['name']}")
        print(f"  Input channels: {info['maxInputChannels']}")
        print(f"  Sample rate: {int(info['defaultSampleRate'])} Hz")
        if is_default:
            print("  ★ DEFAULT INPUT DEVICE ★")
        print()

print("\n" + "="*50)
print("WHAT TO CHECK:")
print("="*50)
print("1. Is there a microphone device listed?")
print("2. Does it show Input channels > 0?")
print("3. Is it marked as DEFAULT INPUT DEVICE?")
print("\nIf not, go to:")
print("  Settings → Sound → Input")
print("  Make sure a microphone is connected and set as default")
