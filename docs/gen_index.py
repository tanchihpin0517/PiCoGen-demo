import os
import sys
import argparse
import re
import shutil
from pathlib import Path

row_template = """\
<div class="row">
    <div class="col-sm border">
        <audio controls="" class="sample">
            <source src="assets/listenning_test_for_demo/{%song%}/test_{%n%}/song.mp3" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
    </div>
    <div class="col-sm border">
        <audio controls="" class="sample">
            <source src="assets/listenning_test_for_demo/{%song%}/test_{%n%}/kr.mp3" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
    </div>
    <div class="col-sm border">
        <audio controls="" class="sample">
            <source src="assets/listenning_test_for_demo/{%song%}/test_{%n%}/our.mp3" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
    </div>
    <div class="col-sm border">
        <audio controls="" class="sample">
            <source src="assets/listenning_test_for_demo/{%song%}/test_{%n%}/chord.mp3" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
    </div>
    <div class="col-sm border">
        <audio controls="" class="sample">
            <source src="assets/listenning_test_for_demo/{%song%}/test_{%n%}/midi.mp3" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
    </div>
</div>
"""

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--index_template_file', type=Path, default='./index_template.html')
    parser.add_argument('--sample_good_file', type=Path, default='./sample_good.csv')
    parser.add_argument('--sample_bad_file', type=Path, default='./sample_bad.csv')
    parser.add_argument('--index_file', type=Path, default='./index.html')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()


    out = args.index_template_file.read_text()


    rows = []
    for line in args.sample_good_file.read_text().strip().split('\n'):
        song, n, genre = map(lambda s: s.strip(), line.split(','))
        print("good", song, n, genre)

        r = row_template
        r = re.sub(r'{%song%}', song, r)
        r = re.sub(r'{%n%}', n, r)
        rows.append(r)
    out = re.sub(r'{%sample_good%}', "\n".join(rows), out)

    rows = []
    for line in args.sample_bad_file.read_text().strip().split('\n'):
        song, n, genre = map(lambda s: s.strip(), line.split(','))
        print("bad", song, n, genre)

        r = row_template
        r = re.sub(r'{%song%}', song, r)
        r = re.sub(r'{%n%}', n, r)
        rows.append(r)
    out = re.sub(r'{%sample_bad%}', "\n".join(rows), out)

    args.index_file.write_text(out)

if __name__ == '__main__':
    main()
