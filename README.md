# 2022-ecosystem
Code for the ecosystem Design Skills week

### Connected or simulated ecosystem
To work in either a connected ecosystem or a simulated ecosystem, make sure you have the correct parameter (True or False) chosen for the "connect_to_ecosystem= ???".
his can be found in line 20 in code.py.

### Change filename to creature.py
For all creature_exampleX.py files, make sure to rename the files to creature.py (and remove the old one)

### Pay attention in code.py
When working with example code, pay attention to line 38-40 in code.py. Make sure they are like the below code when working the creature_example2 and creature_example3.
=>          #ecosystem.send_message("ping") # COMMENT THIS LINE when using creature_example2.py
            message_select = creature.get_selected_message() #UN-COMMENT THIS LINE when using creature_example2.py and rename that file to "creature.py"
            ecosystem.send_message(message_select)

### Specifics
* If you use create_example3.py, change line 7 of the ecosystem.py file to:
=> offline_messages = ["Red&&&100", "Red&&&255", "Blue&&&50", "Blue&&&150", "Green&&&90", "Green&&&220"]
If you want to work in an offline ecosystem.
