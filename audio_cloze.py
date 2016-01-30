# -*- coding: utf-8 -*-

# Audio Cloze.
# Copyright (C) 2016  e.a.gebhart@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Name: Audio Cloze
Filename: acloze.py
Version: 0.1

Author: Eric Gebhart
Contact: e.a.gebhart at gmail.com
Github: https://github.com/EricGebhart/audio_cloze.git

Description: Changes the behavior of clozes which contain audio to be
            consistent with the behavior of purely textual clozes.

            ie. Inactive clozes do not make any sound.  If an audio hint is desired
            for a cloze, place the audio in the hint for that cloze. Multiple
            sounds can be added to the answer or the hint.

            With this addon inactive clozes do not make any sound. If an audio hint
            is desired for a cloze, place the audio in the hint for that cloze.
            Multiple sounds can be added to the answer or the hint.

            The result is absolute control over the sounds played by any card
            generated from a multi cloze note.

            This addon works very well in combination with Awesome TTS.
"""

from anki import template
from anki.hooks import wrap

import re

soundReg = r"\[sound:.*\]"
clozeReg = r"(?s)\{\{c%s::(.*?)(::(.*?))?\}\}"


def removeSound(txt):
    """remove sound tags from a string of text"""
    return re.sub(soundReg, "", txt)


def myClozeText(txt, ord, type):
    """Render clozes for the current card,
    remove sound from other clozes so they will not play."""
    reg = clozeReg
    if not re.search(reg % ord, txt):
        return ""

    def repl(m):
        """replace chosen cloze with appropriate text"""
        hint = (m.group(3) if m.group(3) else "")
        answer = m.group(1)
        hintWithOutSound = removeSound(hint)

        # it's a question.
        if type == "q":

            # the hint has text and sound.
            if hintWithOutSound:
                return "<span class=cloze>[%s]</span>" % hint

            # the hint only has sound or is completely empty.
            else:
                return "<span class=cloze>[...]%s</span>" % hint

        # it's an answer.
        else:
            return "<span class=cloze>%s</span>" % answer

    # replace all of this card's clozes with the hint or the answer.
    txt = re.sub(reg % ord, repl, txt)

    def repl2(m):
        """remove the sound from a cloze answer"""
        return removeSound(m.group(1))

    # replace the rest of the clozes with their answers minus sound.
    return re.sub(reg % "\d+", repl2, txt)


def init_acloze(self, *args, **kwargs):
    self.clozeText = myClozeText

template.Template.clozeText = myClozeText
template.Template.__init__ = wrap(template.Template.__init__, init_acloze)
