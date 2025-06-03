import json, datetime, pathlib

def export_session(scores: dict, out_dir="exports"):
    pathlib.Path(out_dir).mkdir(exist_ok=True)
    fname = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_idscr.json")
    with open(pathlib.Path(out_dir)/fname, 'w') as fp:
        json.dump(scores, fp, indent=2)
    return str(pathlib.Path(out_dir)/fname)
