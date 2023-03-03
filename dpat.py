import argparse as ap

offsets = {
    'mld': 0x2E,
    'mmf': 0x13
}

def remove_copy_protection(file: str):
    audio_name, format = file.split(".")[-2], file.split(".")[-1]
    if format not in offsets.keys():
        raise Exception("Invalid file format")
    with open(file, "rb+") as f:
        data = f.read()
    data = data[:offsets[format]] + b'\x00' + data[offsets[format]+1:]
    with open(audio_name[1:] + "_rmvd." + format, "wb+") as f:
        f.write(data)

def convert_to_midi(file: str):
    pass

if __name__ == "__main__":
    parser = ap.ArgumentParser("dpat.py", description="Remove copy protection from dumbphone audio files")
    parser.add_argument("file", help="File to remove copy protection from")
    args = parser.parse_args()
    
    choice = input("1. Remove DRM\n2. Convert to MIDI (todo)\n")

    while choice != "1" and choice != "2":
        choice = input("Invalid choice. Please try again.\n")
    
    if choice == "1":
        remove_copy_protection(args.file)
        print("Done!")
        exit()
    elif choice == "2":
        print("Not implemented yet!")
        exit()
        