import argparse as ap

# Offset Keywords
# Each format has copy protection byte, and is located after a certain keyword
# k:v -> format: (keyword, offset from keyword beginning)

offset_keywords = {
    'mld': (b'sorc', 6),
    'mmf': (b'OPDA', -2)
}

def remove_copy_protection(file: str):
    audio_name, \
    format, \
    file_root_dir = \
    file.split(".")[-2].split("\\")[-1], \
    file.split(".")[-1], \
    "\\".join(file.split("\\")[:-1])

    if format not in offset_keywords.keys():
        raise Exception("Invalid file format.")
    
    with open(file, "rb+") as f:
        data = f.read()

    if offset_keywords[format][0] in data:
        pos = data.find(offset_keywords[format][0]) + offset_keywords[format][1]
    else:
        raise Exception("No keyword found for the format. Is this a valid audio file of " + format + "?")

    data = data[:pos] + bytes([0x00]) + data[pos + 1:]
    with open(file_root_dir + "\\" + audio_name + "_rmvd." + format, "wb+") as f:
        f.write(data)

if __name__ == "__main__":
    parser = ap.ArgumentParser("dcr.py", description="Remove copy protection from dumbphone audio files")
    parser.add_argument("files", nargs="+", help="Files to remove copy protection from")
    args = parser.parse_args()
    
    if args.files is not None:
        for file in args.files:
            remove_copy_protection(file)
    
    print("Done!")