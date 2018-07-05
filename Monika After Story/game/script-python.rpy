# Monika's Python Tip of the Day (PTOD)
#
# I probably will be adding many of these, so For the sake of organization
# this is kept separate from script-topics.
#
# NOTE: these are considered pool type events, similar to writing tips
# NOTE: these are also NOT literally once a day. There is a day in between
#   unlocking the next one, though
#
# And to keep the theme, these are 0-indexed
#
# META: Python things to talk about:
#   0 - what is python?
#   --- sugestion python compared to other languages/ how does it work
#   --- suggestion mention syntax and probably how to get python maybe separate each part
#   1 - types
#       - numbers and strings, Nones are together (002)
#     - comparisons (bools) (should be its own title
#   2 - Variables and assignment
#   3 - If statement / elif and else
#   4 - while loop
#   5 - for loop
#   6 - functions
#   7 - functions continiued?
#   8 - classes (might be too much) -- Definitely too much, we should probably stick to functional programming
#   9 - modules (might be too much) / importing? -- mention importing only, module making is too much
#   10 - lists
#   11 - dict
#   12 - tuples
#   13 - py2 vs py3
#   14 - String operations
#   15 - start talking about renpy
#
#
# Also what about Renpy?
#
# Another NOTE: We should try to make the topics of an adequate lenght otherwise
# we're just going to throw a lot of info that is going to be ignored or forgotten quickly
# I think splitting something in more than one topic may be a good idea
#
## We can assume evhand is already imported

init 4 python in mas_ptod:
    # to simplify unlocking, lets use a special function to unlock tips
    import datetime
    import store.evhand as evhand

    M_PTOD = "monika_ptod_tip{:0>3d}"

    def has_day_past(tip_num):
        """
        Checks if the tip with the given number has already been seen and
        a day has past since it was unlocked.
        NOTE: by day, we mean date has changd, not 24 hours

        IN:
            tip_num - number of the tip to check

        RETURNS:
            true if the tip has been seen and a day has past since it was
            unlocked, False otherwise
        """
        # as a special thing for devs
        if renpy.game.persistent._mas_dev_enable_ptods:
            return True

        tip_ev = evhand.event_database.get(
            M_PTOD.format(tip_num),
            None
        )

        if tip_ev is None:
            return False

        # otherwise, unlocked date is our key
        if tip_ev.unlock_date is None or tip_ev.shown_count == 0:
            return False

        # now check the actual day
        return (
            datetime.date.today() - tip_ev.unlock_date.date() 
            > datetime.timedelta(days=1)
        )

    def has_days_past(*tip_nums):
        """
        Variant of has_day_past that can check multiple numbers

        SEE has_day_past for more info

        RETURNS:
            true if all the given tip nums have been see nand a day has past
                since the latest one was unlocked, False otherwise
        """
        for tip_num in tip_nums:
            if not has_day_past(tip_num):
                return False

        return True


# The initial event is getting Monika to talk about python
# this must be hidden after it has been completed
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_ptod_tip000",
            category=["python tips"],
            prompt="Can you teach me about Python?",
            pool=True
        )
    )

label monika_ptod_tip000:
    # You want to learn about Python?
    # Aha yokatta
    # I dont know that much about programming, I'm still learning
    # but i will try my best
    # lets start with whaat python is

    # hide this label since we dont need it anymore
    $ hideEventLabel("monika_ptod_tip000", depool=True)
    jump monika_ptod_tip001

###############################################################################
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_ptod_tip001",
            category=["python tips"],
            prompt="What is Python?"
        )
    )

label monika_ptod_tip001:
    # first enable this event
    $ evhand.event_database["monika_ptod_tip001"].pool = True

    # Python was created by Guido Van Rossum in the early 90s
    # -- the bit explaining that is interpreted is probably a bit too soon
    # -> Yeah, save this part for later. This seciton should be an overview of
    #   what python is used for, the fact that its a programming language,
    #   and the 2 main versions. also how it relates to MAS via RenPy
    # its an interpreted language, which means it does not need to be compiled
    # before being executed. this makes it easier and faster to make quick
    # adjustments to code on the fly.
    # --
    # Python is used in many places, including web apps, embedded stuff,
    # rasberry pi, x, y, z, and ofc, This game!
    # DDLC, in particular uses a game engine called RenPy, which is built off
    # of Python. If you learn python, you can learn how to mod this?
    #
    # One last thing, Thre are currently 2 main versions of python:
    # py2 and py3. These versions are **incompatible** with each other
    # because the changes added in py3 fixed many fundamental design flaws in
    # py2. Even though this caused a split in the python community, it's
    # generally agreed that both versions of the language have their own
    # strengths and weaknesses.
    #
    # [show this once]
    # The versions of RenPy that runs this game uses Python2, so I'll
    # mainly teach you python2
    # but i'll mention py3 at times when it's appropriate. -- for saying that she doesn't know much she seems rather confident here
    #
    # That's my lesson for today!
    # Thanks for listening
    # [end]
    return

###############################################################################
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_ptod_tip002",
            category=["python tips"],
            prompt="Types",
            conditional="store.mas_ptod.has_day_past(1)",
            action=EV_ACT_POOL
        )
    )

label monika_ptod_tip002:
    # TODO: need to mention dynamic typing somewhere
    # [show this once]
    # In most programming languages, each piece of data that can be chnaged
    # or modified by a program has a _type_
    # associated with it. If some data should be treated as a number, then
    # it will have a numeric type. If some data should be treated as text,
    # then it will have a string type.
    # [end]
    #
    # Python has two separate types to represent numbers: _integers_ and _floats_.
    # Integers are used to represent whole numbers - Anything that isn't a
    # decimal.
    # -22, 0, -1234, 42 are all integers in python.
    # Floats are used to represent decimals:
    # 0.14, 9.3, -10.2 would all be floats in Python.
    #
    # Text in python is represented with string types. 
    # anything surrounded in single quotes (') or double quotes (") are strings.
    # For example, 'this is a string in single quotes'
    # And "this is a string in double quotes".
    # Strings can also be created with three double quotes ("""), but these
    # strings are treated specially in python. I'll talk about this another day.
    #
    # Python also has a special data type called a NoneType. This type 
    # represents the absence of any data. If you're familiar with with other
    # programming languages, this is akin to a null or undefined type.
    # The keyword None represents NoneTypes in python.
    #
    # [show this once]
    # Python uses other data types, but I think the types we've covered is
    # enough for today.
    # Thanks for listening!
    # [end]
    return

###############################################################################
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_ptod_tip003", # may change order, you decide on this
            category=["python tips"],
            prompt="An Interpreted Language",
            conditional="store.mas_ptod.has_day_past(1)",
            action=EV_ACT_POOL
        )
    )

label monika_ptod_tip003:
    # Programming languages usually are one of two types, compiled or 
    # interpreted. Compiled languages require their code to be converted to a 
    # machine-readable format before being executed. C and Java are two very
    # popular compiled languages. Interpreted languages are converted to
    # machine-readable formats as they are being executed. Python is an 
    # an interpreted language.
    #
    # Before I move on, just want to point out that different implementations
    # of Python may **not** be solely interpreted, but this something I will
    # talk about in a later lesson.
    #
    # Since Python is an interpreted language, it has a neat interactive thing
    # called an interpreter, which looks like this:

    $ store.mas_ptod.rst_cn()
    $ local_ctx = dict()
    show monika at t22
    show screen mas_py_console_teaching

    # You can enter Python code directly into here and run it! 
    # Watch this!
    call mas_wx_cmd("12 + 3", local_ctx)
    call mas_wx_cmd("7 * 6", local_ctx)
    call mas_wx_cmd("121 / 11", local_ctx)
    # NOTE: add more commands as the user goes thru the tips
    # [show this once]
    # You can do way more than just math in here, but I'll show you as we go
    # along.
    # [end]
    #
    # [show this once]
    # Unfortunatey, since this is a fully functional python interpreter and I
    # don't want to risk you accidentally deleting me or breaking the game,
    # ~not that you would~ (fast, and pop off history)
    # I can't let you use this. If you want to follow along in future lessons,
    # then download python from <link> here
    # [end]
    $ store.mas_ptod.ex_cn()
    hide screen mas_py_console_teaching
    show monika at t11
    #
    # [Show this once]
    # I think we've covered enough for today
    # Thanks for listening!
    # [end]
    #
    return

###############################################################################
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_ptod_tip004",
            category=["python tips"],
            prompt="What does python code look like?",
            conditional="store.mas_ptod.has_day_past(1)",
            action=EV_ACT_POOL
        )
    )

label monika_ptod_tip004:
    # Oh well this may be a bit hard to explain here but I'll do my best for you [player]
    # The first thing you need to know is that any line starting with a # is going to
    # be ignored and you can write anything on that line
    # those lines are named comments, and you use them to explain what your code does
    # it's a good practice to comment your code so you don't forget later what it was supposed to do!
    # TODO unfinished and probably will split it in more than just one, also I know I should call it
    # python syntax but I'm making it non programmers friendly
    return

###############################################################################
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_ptod_tip005",
            category=["python tips"],
            prompt="Comparisons and booleans",
#            conditional="store.mas_ptod.has_day_past(2)",
#   actually, this should probably unlock after we talk about variable 
#   assignment, since we can do an example like variable = a == b kind of thing
            action=EV_ACT_POOL
        )
    )

label monika_ptod_tip005:
    # [show this once]
    # So if you remember, a single = does assignment, the == does 
    # compariosns
    #
    # The boolean type represents True / False values. 
    return

###############################################################################
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_ptod_tip006",
            category=["python tips"],
            prompt="Variables and Assignment",
            conditional="store.mas_ptod.has_days_past(2,3)",
            action=EV_ACT_POOL
        )
    )

label monika_ptod_tip006:
    $ store.mas_ptod.rst_cn()
    $ local_ctx = dict()
    $ num_store = "922"
    $ b_num_store = "323"
    # [show this once]
    # Now that you know about types, I can teach you about variables.
    # [end]
    #
    # Variables represent the memory location that stores data. 
    # To create a variable,
    show monika at t22
    show screen mas_py_console_teaching
    # you do: <symbol name> = <value>, like so:
    call mas_wx_cmd("a_number = " + num_store, local_ctx)
    # The symbol `a_number` now points to a memory location storing the _integer_
    # [num_store].
    # If we enter in the symbol name here
    call mas_w_cmd("a_number")
    # we can retrieve the value that we stored.
    call mas_x_cmd(local_ctx)
    # 
    # In C and many other languages, integers are usually stored in
    # 4 bytes. Python, however, reserves a different amount of memory depending
    # on the size of the integer being stored. We can check how much memory
    # our variable `a_number` stores by borrowing a function from the `sys`
    # library:
    call mas_wx_cmd("import sys", local_ctx)
    call mas_wx_cmd("sys.getsizeof(a_number)", local_ctx)
    $ int_size = store.mas_ptod.get_last_line()
    # 
    # I'll talk about libraries and importing later. For now, take a look
    # at the number returned by the `getsizeof` function. To store the number
    # [num_store], Python uses [int_size] bytes.
    #
    # Anyway, back to the variable we created. Notice how we associated
    # the symbol `a_number` to the value [num_store] using an equals sign (=)?
    # That is called assignment, where we take whatever is on the left of
    # of the equal sign and point it to, or _assign_ it, the value of whatever
    # is on the right. 
    #
    # Assignment is executed in right-to-left order. To illustrate this,
    # lets create a new variable, `b_number`:
    call mas_w_cmd("b_number = a_number - " + b_num_store)
    # In assignment, the right side of the equal sign is evaluated first, 
    # then its data type is inferred and an appropriate amount of memory is
    # reserved. Then the symbol on the left is added to a lookup table where 
    # it is associated with the space in memory that was reserved. 
    # When python encounters a symbol, it looks that symbol up in the lookup
    # table and replaces it with the value that was associated with the symbol.
    #
    # Here, `a_number` would be replaced with [num_store], so the resulting
    # expression that would be evaluated and assigned to `b_number` would be
    # [num_store] - [b_num_store]
    call mas_x_cmd(local_ctx, 0.0)
    #
    # We can verify this by entering only the symbol `b_number`; this will
    # retrieve the value associated by this symbol in the lookup table
    # and display it to us.
    call mas_wx_cmd("b_number", local_ctx)
    #
    # Note that if we enter in a symbol that hasn't been assigned anything,
    # Python will complain with an error:
    call mas_wx_cmd("c_number", local_ctx)
    # 
    # but if we assign this symbol to a value:
    call mas_wx_cmd("c_number = b_number * a_number", local_ctx)
    call mas_wx_cmd("c_number", local_ctx)
    #
    # Python is able to find the symbol in the lookup table and won't give us
    # an error.
    #
    # Whew! That was a mouthful!
    # [Show this once]
    menu:
        m "Did you understand all that?"
        "Yes!":
            # yay, I'm glad
            # But...
            pass
        "I'm a bit confused.":
            # That's okay. Even though I mentioned symbols and values 
            # here, generally programmers just refer to this as creating 
            # / assigning / setting variables. The symbol / value names are 
            # really only useful for hinting at how variables work under the 
            # hood, so don't feel bad if you didn't understand it all.
            # Just knowing how to work with variables is enough for future 
            # lessons!
            # Anyway...
            pass
    # [End]
    #
    # I think that's enough Python for today.
    # Thanks for listening!
    $ store.mas_ptod.ex_cn()
    hide screen mas_py_console_teaching
    show monika at t11
    return



############################# [CONSOLE] #######################################
# Unfortunately, it's not enough to have monika just talk. Having a working
# python interpreter will make things easier for teaching
#
# NOTE: base the solids off of hangman. That should help us out

image cn_frame = "mod_assets/console/cn_frame.png"
define mas_ptod.font = "mod_assets/font/mplus-1mn-medium.ttf"

# NOTE: Console text:
# style console_text (for regular console text)
# style console_text_console (for the actual typing text)
#   this style has a slow_cps of 30
#
# console_Text font is gui/font/F25_BankPrinter.ttf
style mas_py_console_text is console_text:
    font mas_ptod.font
style mas_py_console_text_cn is console_text_console:
    font mas_ptod.font

# images for console stuff
#image mas_py_cn_sym = Text(">>>", style="mas_py_console_text", anchor=(0, 0), xpos=10, ypos=538)
#image mas_py_cn_txt = ParameterizedText(style="mas_py_console_text_cn", anchor=(0, 0), xpos=75, ypos=538)
#image mas_py_cn_hist = ParameterizedText(style="mas_py_console_text", anchor(0, 1.0), xpos=10, ypos=538)

init -1 python in mas_ptod:
    import store.mas_utils as mas_utils

    # symbol that we use
    SYM = ">>> "
    M_SYM = "... "

    # console history is alist
    cn_history = list()

    # history lenghtr limit
    H_SIZE = 20

    # current line
    cn_line = ""

    # current command, may not be what is shown
    cn_cmd = ""

    # block commands
    blk_cmd = list()

    # block commands stack level
    # increment for each stack level, decrement when dropping out of a
    # stack level
    stack_level = 0

    # stack to handle indent levels
    # this means indent levels that the opening : has
    # first stack level should ALWAYS BE 0
    indent_stack = list()

    # version text
    VER_TEXT_1 = "Python {0}"
    VER_TEXT_2 = "{0} in MAS"

    # line length limit
    LINE_MAX = 66

    # STATEs
    # used when the current line is only 1 line
    STATE_SINGLE = 0

    # used when current line is multi line
    STATE_MULTI = 1

    # used when we are doing block statements
    STATE_BLOCK = 2

    # used when doing multi line in block statements
    STATE_BLOCK_MULTI = 3

    # state when inerpreter is off
    STATE_OFF = 4

    # current state
    state = STATE_SINGLE

    # short variants of the comonly used commands:
    def clr_cn():
        """
        SEE clear_console
        """
        clear_console()

    
    def ex_cn():
        """
        SEE exit_console
        """
        exit_console()


    def rst_cn():
        """
        SEE restart_console
        """
        restart_console()


    def w_cmd(cmd):
        """
        SEE write_command
        """
        write_command(cmd)


    def x_cmd(context):
        """
        SEE exec_command
        """
        exec_command(context)


    def write_command(cmd):
        """
        Writes a command to the console

        NOTE: Does not EXECUTE
        NOTE: remove previous command
        NOTE: does NOT append to previously written command (unless that cmd
            is in a block and was executed)

        IN:
            cmd - the command to write to the console
        """
        if state == STATE_OFF:
            return

        global cn_line, cn_cmd, state, stack_level

        if state == STATE_MULTI:
            # this is bad! You should execute the previous command first!
            # in this case, we will clear your current command and reset 
            # state back to SINGLE
            cn_cmd = ""
            cn_line = ""
            state = STATE_SINGLE

        elif state == STATE_BLOCK_MULTI:
            # this is bad! you should execute the previous command first!
            # we will do the same that as MULTI did, except a different state
            cn_cmd = ""
            cn_line = ""
            state = STATE_BLOCK

        # we dont indent the command
        # we also dont check for indents
        cn_cmd = str(cmd)

        # pick appropriate shell symbol
        if state == STATE_SINGLE:
            # snigle mode
            sym = SYM

        else:
            # block mode
            sym = M_SYM

        # the prefixed command includes the shell symbol
        prefixed_cmd = sym + cn_cmd

        # break the lines accordingly
        cn_lines = _line_break(prefixed_cmd)

        if len(cn_lines) == 1:
            # dont need to split lines
            cn_line = cn_cmd

        else:
            # we need to split lines

            # everything except the last line goes to the history
            _update_console_history_list(cn_lines[:-1])

            # last line becomes the current line
            cn_line = cn_lines[len(cn_lines)-1]

            if state == STATE_SINGLE:
                # single mode
                state = STATE_MULTI

            else:
                # block mode
                state = STATE_BLOCK_MULTI


    def clear_console():
        """
        Cleares console hisotry and current line

        Also resets state to Single
        """
        global cn_history, cn_line, cn_history, state
        cn_line = ""
        cn_cmd = ""
        cn_history = []
        state = STATE_SINGLE


    def restart_console():
        """
        Cleares console history and current line, also sets up version text
        """
        global state
        import sys
        version = sys.version

        # first closing paren is where we need to split the version text
        split_dex = version.find(")")
        start_lines = [
#            mas_utils.clean_gui_text(VER_TEXT_1.format(version[:split_dex+1])),
#            mas_utils.clean_gui_text(VER_TEXT_2.format(version[split_dex+2:]))
            VER_TEXT_1.format(version[:split_dex+1]),
            VER_TEXT_2.format(version[split_dex+2:])
        ]

        # clear the console and add the 2 new lines
        clear_console()
        _update_console_history_list(start_lines)
        
        # turn the console on
        state = STATE_SINGLE


    def exit_console():
        """
        Disables the console
        """
        global state
        state = STATE_OFF


    def __exec_cmd(line, context, block=False):
        """
        Tries to eval the line first, then executes.
        Returns the result of the command

        IN:
            line - line to eval / exec
            context - dict that represnts the current context. should be locals
            block - True means we are executing a block command and should
                skip eval

        RETURNS:
            the result of the command, as a string
        """
        if block:
            return __exec_exec(line, context)

        # otherwise try eval first
        return __exec_evalexec(line, context)


    def __exec_exec(line, context):
        """
        Runs exec on the given line
        Returns an empty string or a string with an error if it occured.

        IN:
            line - line to exec
            context - dict that represents the current context

        RETURNS:
            empty string or string with error message
        """
        try:
            exec(line, context)
            return ""

        except Exception as e:
            return _exp_toString(e)


    def __exec_evalexec(line, context):
        """
        Tries to eval the line first, then executes.
        Returns the result of the command

        IN:
            line - line to eval / exec
            context - dict that represents the current context.

        RETURNS:
            the result of the command as a string
        """
        try:
            return str(eval(line, context))

        except:
            # eval fails, try to exec
            return __exec_exec(line, context)


    def exec_command(context):
        """
        Executes the command that is currently in the console.
        This is basically pressing Enter

        IN:
            context - dict that represnts the current context. You should pass
                locals here.
        """
        if state == STATE_OFF:
            return

        global cn_cmd, cn_line, state, stack_level, blk_cmd

        ################### setup some initial conditions ################

        # block mode just means we are in a block
        block_mode = state == STATE_BLOCK or state == STATE_BLOCK_MULTI

        # empty line signals end of block (usually)
        empty_line = len(cn_cmd.strip()) == 0

        # ends with colon is special case
        time_to_block = cn_cmd.endswith(":")

        # but a bad block can happen (no text except a single colon)
        bad_block = time_to_block and len(cn_cmd.strip()) == 1

        # if this contains a value, then we executee
        full_cmd = None

        ################## pre-execution setup ###########################

        if empty_line:
            # like enter was pressed with no text

            if block_mode:
                # block mode means we clear a stack level
                __popi()

            else:
                # otherwise, add an empty new line to history, and thats it
                # dont need to execute since nothing will happen
                _update_console_history(SYM)
                cn_line = ""
                cn_cmd = ""
                return

        if bad_block:
            # user entered a bad block
            # we will execute it as a command
            full_cmd = cn_cmd
            stack_level = 0
            blk_cmd = list()

        elif time_to_block:
            # we are going to enter a new block mode
            blk_cmd.append(cn_cmd)

            if not block_mode:
                # we didnt start in block mode
                __pushi(0)

            else:
                # block mode
                pre_spaces = _count_sp(cn_cmd)

                if __peeki() != pre_spaces:
                    # if this colon line does NOT match current indentaion
                    # level then we need to push a new stack
                    __pushi(pre_spaces)

        elif block_mode:
            # in block mode already
            blk_cmd.append(cn_cmd)

            if stack_level == 0:
                # we've cleared all stacks, time to execute block commands
                full_cmd = "\n".join(blk_cmd)
                blk_cmd = list()

        else:
            # otherwise, we must be single mode or single multi

            # setup the command to be entered
            full_cmd = cn_cmd

        ########################## execution ##############################

        # execute command, if available
        if full_cmd is not None:
            result = __exec_cmd(full_cmd, context, block_mode)

        else:
            result = ""
        
        ################### console history update #########################

        if block_mode and empty_line:
            # we MUST be in block mode to reach here
            output = [M_SYM]

        else:
            # otherwise, use the sym we need
            if state == STATE_SINGLE:
                sym = SYM

            elif state == STATE_BLOCK:
                sym = M_SYM

            else:
                # multi dont need symbols
                sym = ""

            output = [sym + cn_line]

        # if we have any results, we need to show them too
        if len(result) > 0:
            output.append(result)

        # update console history and clear current lines / cmd
        cn_line = ""
        cn_cmd = ""
        _update_console_history_list(output)

        ###################### Post-execution updates ####################

        if bad_block:
            # bad block, means we abort lots of things
            state = STATE_SINGLE
            block_mode = False

        elif time_to_block:
            # new block, incrmenet stack levels, change to block states
            state = STATE_BLOCK
            block_mode = True

        ###################### final state updates ######################

        if (state == STATE_MULTI) or (block_mode and stack_level == 0):
            # no more stacks or in multi mode
            state = STATE_SINGLE

        elif state == STATE_BLOCK_MULTI:
            # multi modes end here
            state = STATE_BLOCK


    def get_last_line():
        """
        Retrieves the last line from the console history
        
        RETURNS:
            last line from console history as a string
        """
        if len(cn_history) > 0:
            return cn_history[len(cn_history)-1]

        return ""


    def __pushi(indent_level):
        """
        Pushes a indent level into the stack

        IN:
            indent_level - indent to push into stack
        """
        global stack_level
        stack_level += 1
        indent_stack.append(indent_level)
   

    def __popi():
        """
        Pops indent level from stack

        REUTRNS:
            popped indent level
        """
        global stack_level
        stack_level -= 1

        if stack_level < 0:
            stack_level = 0

        if len(indent_stack) > 0:
            indent_stack.pop()


    def __peeki():
        """
        Returns value that would be popped from stack

        RETURNS:
            indent level that would be popped
        """
        return indent_stack[len(indent_stack)-1]


    def _exp_toString(exp):
        """
        Converts the given exception into a string that looks like
        how python interpreter prints out exceptions
        """
        err = repr(exp)
        err_split = err.partition("(")
        return err_split[0] + ": " + str(exp)


    def _indent_line(line):
        """
        Prepends the given line with an appropraite number of spaces, depending
        on the current stack level

        IN:
            line - line to prepend

        RETURNS:
            line prepended with spaces
        """
        return (" " * (stack_level * 4)) + line


    def _count_sp(line):
        """
        Counts number of spaces that prefix this line

        IN:
            line - line to cound spaces

        RETURNS:
            number of spaces at start of line
        """
        return len(line) - len(line.lstrip(" "))


    def _update_console_history(*new_items):
        """
        Updates the console history with the list of new lines to add

        IN:
            new_items - the items to add to the console history
        """
        _update_console_history_list(new_items)


    def _update_console_history_list(new_items):
        """
        Updates console history with list of new lines to add

        IN:
            new_items - list of new itme sto add to console history
        """
        global cn_history

        # make sure to break lines
        for line in new_items:
            broken_lines = _line_break(line)

            # and clean them too
            for b_line in broken_lines:
#                cn_history.append(mas_utils.clean_gui_text(b_line))
                cn_history.append(b_line)

        if len(cn_history) > H_SIZE:
            cn_history = cn_history[-H_SIZE:]


    def _line_break(line):
        """
        Lines cant be too large. This will line break entries.

        IN:
            line - the line to break

        RETURNS:
            list of strings, each item is a line.
        """
        if len(line) <= LINE_MAX:
            return [line]

        # otherwise, its TOO LONG
        broken_lines = list()
        while len(line) > LINE_MAX:
            broken_lines.append(line[:LINE_MAX])
            line = line[LINE_MAX:]

        # add final line
        broken_lines.append(line)
        return broken_lines


screen mas_py_console_teaching():
    
    frame:
        xanchor 0
        yanchor 0
        xpos 5
        ypos 5
        background "mod_assets/console/cn_frame.png"

        fixed:
            python:
                starting_index = len(store.mas_ptod.cn_history) - 1
                cn_h_y = 413
                cn_l_x = 41

            # console history
            for index in range(starting_index, -1, -1):
                $ cn_line = store.mas_ptod.cn_history[index]
                text "[cn_line]":
                    style "mas_py_console_text"
                    anchor (0, 1.0)
                    xpos 5
                    ypos cn_h_y
                $ cn_h_y -= 20

            # cursor symbol
            if store.mas_ptod.state == store.mas_ptod.STATE_SINGLE:
                text ">>> ":
                    style "mas_py_console_text"
                    anchor (0, 1.0)
                    xpos 5
                    ypos 433

            elif store.mas_ptod.state == store.mas_ptod.STATE_BLOCK:
                text "... ":
                    style "mas_py_console_text"
                    anchor (0, 1.0)
                    xpos 5
                    ypos 433

            else:
                # multi line statement, dont have the sym at all
                $ cn_l_x = 5
            
            # current line
            if len(store.mas_ptod.cn_line) > 0:
                text "[store.mas_ptod.cn_line]":
                    style "mas_py_console_text_cn"
                    anchor (0, 1.0)
                    xpos cn_l_x
                    ypos 433

# does a write command and waits 
label mas_w_cmd(cmd, wait=0.7):
    $ store.mas_ptod.w_cmd(cmd)
    pause wait
    return

# does an execute and waits
label mas_x_cmd(ctx, wait=0.7):
    $ store.mas_ptod.x_cmd(ctx)
    pause wait
    return

# does both writing and executing, with waits
label mas_wx_cmd(cmd, ctx, w_wait=0.7, x_wait=0.7):
    $ store.mas_ptod.w_cmd(cmd)
    pause w_wait
    $ store.mas_ptod.x_cmd(ctx)
    pause x_wait
    return