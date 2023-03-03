import argparse as ap

def remove_drm(file: str):
    with open(file, "rb+") as f:
        f.seek(0x2E)
        f.write(b'\x00')
        f.seek(0)

def convert_to_midi(file: str):
    pass

if __name__ == "__main__":
    parser = ap.ArgumentParser("mld-tools")
    parser.add_argument("file", help="File to remove copy protection from")
    args = parser.parse_args()
    
    choice = input("1. Remove DRM\n2. Convert to MIDI (todo)\n")

    while choice != "1" and choice != "2":
        choice = input("Invalid choice. Please try again.\n")
    
    if choice == "1":
        remove_drm(args.file)
        print("Done!")
        exit()
    elif choice == "2":
        print("Not implemented yet!")
        exit()
        