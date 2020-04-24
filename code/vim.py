#this is largely modeled on vimspeak

from typing import Set

from talon import Module, Context, actions
import sys

mod = Module()
ctx = Context()

ctx.lists['self.vim_surround_targets'] = {
    "stars" : "*",
    "asterisks" : "*",
    "word" : "w",
    "big word" : "W",
    "block" : "b",
    "big block" : "B",
    "quotes" : "\"",
    "double quotes" : "\"",
    "single quotes" : "'",
    "loose parens" : "(",
    "loose parenthesis" : "(",
    "loose angle brackets" : "<",
    "loose curly braces" : "{",
    "loose braces" : "{",
    "loose square brackets" : "[",
    "loose brackets" : "[",
    "tight parens" : ")",
    "tight parenthesis" : ")",
    "tight angle brackets" : ">",
    "tight curly braces" : "}",
    "tight braces" : "}",
    "tight square brackets" : "]",
    "tight brackets" : "]",
    "parens" : ")",
    "parenthesis" : ")",
    "angle brackets" : ">",
    "curly braces" : "}",
    "braces" : "}",
    "square brackets" : "]",
    "brackets" : "]",
    "backticks" : "`",
    "sentence" : "s",
    "paragraph" : "p",
    "tags" : "t",
    "h1 tags" : "<h1>",
    "h2 tags" : "<h2>",
    "div tags" : "<div>",
    "bold tags" : "<b>",
}

ctx.lists['self.vim_counted_action_verbs'] = {
    "after" : "a",
    "append" : "a",
    "after line" : "A",
    "append line" : "A",
    "insert" : "i",
    "insert before line" : "I",
    "insert line" : "I",
    "insert column zero" : "gI",
    "open" : "o",
    "open below" : "o",
    "open above" : "O",
    "substitute" : "s",
    "substitute line" : "S",
    "undo" : "u",
    "undo line" : "U",
    "redo" : "<C r>",
    "erase" : "x",
    "erase reversed" : "X",
    "erase back" : "X",
    "put" : "p",
    "paste" : "p",
    "put before" : "P",
    "paste before" : "P",
    "put above" : "P",
    "paste above" : "P",
    "repeat" : ".",
    "scroll up" : "<C y>",
    "scroll down" : "<C e>",
    "page down" : "<C f>",
    "page up" : "<C b>",
    "half page down" : "<C d>",
    "half page up" : "<C u>",
    "indent line" : ">>",
    "unindent line" : "<<",
    "toggle case" : "~",
#    "comment line",             @"\\\",
#    "comment lines",            @"\\\",
#    "uncomment line",           @"\\\",
#    "uncomment lines",          @"\\\",
    "scroll left" : "zh",
    "scroll right" : "zl",
    "scroll half screen left" : "zH",
    "scroll half screen right" : "zL",
    "scroll start" : "zs",
    "scroll end" : "ze",
    "play again" : "@@",
}

ctx.lists['self.vim_jump_range'] = {
    "jump to line of" : "'",
    "jump to character of" : "`",
}

ctx.lists['self.vim_jump_verbs'] = {
    "start of last selection" : "<",
    "end of last selection" : ">",
    "latest jump" : "'",
    "last exit" : "\"",
    "last insert" : "^",
    "last change" : ".",
}

# XXX see about replacing the play word eth something that doesn't conflict
# with an existing grammar
ctx.lists['self.vim_counted_actions_args'] = {
    "play macro" : "@", # takes char arg
}

ctx.lists['self.vim_command_verbs'] = {
    "change": "c",
    "delete": "d",
    "indent": ">",
    "unindent": "<",
    "an indent": "<",
    "un indent": "<",
    "join": "J",
    "format": "=",
    "put": "p",
    "paste": "p",
    "undo": "u",
    "yank": "y",
    "copy": "y",
}

ctx.lists['self.vim_motion_verbs'] = {
    "back": "b",
    "back word": "b",
    "big back": "B",
    "big back word": "B",
    "end": "e",
    "big end": "E",
    "word": "w",
    "words": "w",
    "big word": "W",
    "big words": "W",
    "back end": "ge",
    "back end": "ge",
    "back big end": "gE",
# XXX - see if there's a way to replaces with normal arrow keys
    "left": "h",
    "down": "j",
    "up": "k",
    "right": "l",
    "next": "n",
    "next reversed": "N",
    "previous": "N",
    "column zero": "0",
    "column": "|",
    "start of line": "^",
    "end of line": "$",
    "search under cursor": "*",
    "search under cursor reversed": "#",
    "again": ";",
    "again reversed": ",",
    "down sentence": ")",
    "up sentence": "(",
    "down paragraph": "}",
    "up paragraph": "{",
    "start of next section": "]]",
    "start of previous section": "[[",
    "end of next section": "][",
    "end of previous section": "[]",
    "matching": "%",
    "down line": "+",
    "up line": "-",
    "first character": "_",
    "cursor home": "H",
    "cursor middle": "M",
    "cursor last": "L",
    # XXX see if we can mix these matches with talon style () somehow
    "start of document": "gg",
    "start of file": "gg",
    "top of document": "gg",
    "top of file": "gg",
    "end of document": "G",
    "end of file": "G",

# XXX - these need to be keys
    "retrace movements": "ctrl-o",
    "retrace movements forward": "ctrl-i",
}

# all of these motions take a character argument
ctx.lists['self.vim_motion_verbs_with_character'] = {
    "jump to mark": "'",
    "find": "f",
    "find reversed": "F",
    "till": "t",
    "till reversed": "T",
}

# all of these motions take a phrase argument
ctx.lists['self.vim_motion_verbs_with_phrase'] = {
    "search": "/",
    "search reversed": "?",
}

ctx.lists['self.vim_text_object_count'] = {
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
}

ctx.lists['self.vim_text_object_range'] = {
    "inner" : "i",
    "around" : "a",
    "this" : "a",
}

ctx.lists['self.vim_text_object_select'] = {
    "word" : "w",
    "words" : "w",
    "big word" : "W",
    "big words" : "W",
    "block" : "b",
    "blocks" : "b",
    "big block" : "B",
    "big blocks" : "B",
    "quotes" : "\"",
    "double quotes" : "\"",
    "single quotes" : "'",
    "parens" : "(",
    "parenthesis" : "(",
    "angle brackets" : "<",
    "curly braces" : "{",
    "braces" : "{",
    "square brackets" : "[",
    "brackets" : "[",
    "backticks" : "`",
    "sentence" : "s",
    "sentences" : "s",
    "paragraph" : "p",
    "paragraphs" : "p",
    "tag block" : "t",
}

mod.list('vim_command_verbs',    desc='Common VIM commands')
mod.list('vim_counted_motion_verbs',    desc='Common VIM motions')
mod.list('vim_counted_action_verbs',    desc='Common VIM motions')
mod.list('vim_normal_counted_action',    desc='Common VIM motions')
mod.list('vim_motion_verbs',    desc='Common VIM motions')
mod.list('vim_motion_verbs_with_character',    desc='Common VIM motions')
mod.list('vim_motion_verbs_with_phrase',    desc='Common VIM motions')
mod.list('vim_motion_verbs_all',    desc='Common VIM motions')
mod.list('vim_text_object_count',    desc='Common VIM motions')
mod.list('vim_text_object_range',    desc='Common VIM motions')
mod.list('vim_text_object_select',    desc='Common VIM motions')
mod.list('vim_jump_range',    desc='Common VIM motions')
mod.list('vim_jump_verbs',    desc='Common VIM motions')
mod.list('vim_jump_targets',    desc='Common VIM motions')
mod.list('vim_normal_counted_command',    desc='Common VIM motions')
mod.list('vim_select_motion',    desc='Common VIM motions')
mod.list('vim_surround_targets',    desc='Common VIM motions')
mod.list('vim_any',    desc='Common VIM motions')

@mod.capture
def vim_surround_targets(m) -> str:
     "Returns a string"

@mod.capture
def vim_select_motion(m) -> str:
     "Returns a string"

@mod.capture
def vim_counted_action_verbs(m) -> str:
     "Returns a string"

@mod.capture
def vim_normal_counted_action(m) -> str:
     "Returns a string"

@mod.capture
def vim_jump_targets(m) -> str:
     "Returns a string"

@mod.capture
def vim_jump_verbs(m) -> str:
     "Returns a string"

@mod.capture
def vim_jump_range(m) -> str:
     "Returns a string"

@mod.capture
def vim_text_object_count(m) -> str:
     "Returns a string"

@mod.capture
def vim_text_object_range(m) -> str:
     "Returns a string"

@mod.capture
def vim_text_object_select(m) -> str:
     "Returns a string"

@mod.capture
def vim_command_verbs(m) -> str:
    "Returns a list of verbs"

@mod.capture
def vim_counted_motion_verbs(m) -> str:
    "Returns a list of verbs"

@mod.capture
def vim_motion_verbs(m) -> str:
    "Returns a list of verbs"

@mod.capture
def vim_motion_verbs_with_character(m) -> str:
    "Returns a list of verbs"

@mod.capture
def vim_motion_verbs_with_phrase(m) -> str:
    "Returns a list of verbs"

@mod.capture
def vim_motion_verbs_all(m) -> str:
    "Returns a list of verbs"

@mod.capture
def vim_any(m) -> str:
    "Any one key"

@mod.capture
def vim_text_object_range(m) -> str:
    "Returns a string"

@mod.capture
def vim_text_object_select(m) -> str:
    "Returns a string"

@mod.capture
def vim_text_objects(m) -> str:
    "Returns a string"

@mod.capture
def vim_normal_counted_command(m) -> str:
    "Returns a string"

@ctx.capture(rule='{self.vim_text_object_select}')
def vim_text_object_select(m) -> str:
    "Returns a string"
    return m.vim_text_object_select

@ctx.capture(rule='{self.vim_text_object_range}')
def vim_text_object_range(m) -> str:
    "Returns a string"
    return m.vim_text_object_range

@ctx.capture(rule='{self.vim_text_object_count}')
def vim_text_object_count(m) -> str:
     "Returns a string"
     return m.vim_text_object_count

@ctx.capture(rule='{self.vim_command_verbs}')
def vim_command_verbs(m) -> str:
    return m.vim_command_verbs

@ctx.capture(rule='{self.vim_motion_verbs}')
def vim_motion_verbs(m) -> str:
    return m.vim_motion_verbs

@ctx.capture(rule='{self.vim_motion_verbs_with_character} (<user.letter>|<user.number>|<user.symbol>)')
def vim_motion_verbs_with_character(m) -> str:
    return m.vim_motion_verbs_with_character + "".join(list(m)[1:])

@ctx.capture(rule='{self.vim_motion_verbs_with_phrase} <phrase>')
def vim_motion_verbs_with_phrase(m) -> str:
    return "".join(list(m.vim_motion_verbs_with_phrase + m.phrase))

@ctx.capture(rule='(<self.vim_motion_verbs>|<self.vim_motion_verbs_with_character>|<self.vim_motion_verbs_with_phrase>)$')
def vim_motion_verbs_all(m) -> str:
    return "".join(list(m))

@ctx.capture(rule='{self.vim_counted_action_verbs}')
def vim_counted_action_verbs(m) -> str:
    return m.vim_counted_action_verbs

@ctx.capture(rule='[<self.number>] <self.vim_motion_verbs_all>$')
def vim_counted_motion_verbs(m) -> str:
    return "".join(list(m))

@ctx.capture(rule='{self.vim_jump_range}')
def vim_jump_range(m) -> str:
    return m.vim_jump_range

@ctx.capture(rule='{self.vim_jump_verbs}')
def vim_jump_verbs(m) -> str:
    return m.vim_jump_verbs

@ctx.capture(rule='{self.vim_surround_targets}')
def vim_surround_targets(m) -> str:
    return m.vim_surround_targets

@ctx.capture(rule='<self.vim_jump_range> <self.vim_jump_verbs>$')
def vim_jump_targets(m) -> str:
    return "".join(list(m))

@ctx.capture(rule='[<self.vim_text_object_count>] <self.vim_text_object_range> <self.vim_text_object_select>$')
def vim_text_objects(m) -> str:
    return "".join(list(m))

@ctx.capture(rule='[<self.number>] <self.vim_command_verbs> (<self.vim_motion_verbs_all> | <self.vim_text_objects> | <self.vim_jump_targets>)$')
def vim_normal_counted_command(m) -> str:
    return("".join(list(m)))

@ctx.capture(rule='[<self.number>] <self.vim_counted_action_verbs>$')
def vim_normal_counted_action(m) -> str:
    return "".join(list(m))

@ctx.capture(rule='[<self.number>] (<self.vim_motion_verbs> | <self.vim_text_objects> | <self.vim_jump_targets>)$')
def vim_select_motion(m) -> str:
    return "".join(list(m))

@mod.action_class
class Actions:
    def vim_cmd(words: list):
        "Insert an abbreviation"
        for word in words:
            actions.insert(word)
        print(words)

class VimMode:
    def get_mode(self):
        print("Get vim mode")

    def set_mode(self, mode):
        print("Set vim mode")

class LinuxVimMode(VimMode):
    def get_mode(self):
        # query win.title for mode based on having specific vim config
        print("linux mode")