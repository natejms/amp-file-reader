from ampersand import build
from os import path

def main(content, site):
    # Read any external file translations into the dictionary
    for key, value in sorted(content.items()):
        for ky, vl in sorted(content[key].items()):
            for k, v in sorted(content[key][ky]["trans"].items()):
                if content[key][ky]["trans"][k].startswith("file:"):
                    content[key][ky]["trans"][k] = build.read_file(path.join(site.root, path.dirname(site.config["files"][key][ky]), v.replace("file:", "")))
    return content
