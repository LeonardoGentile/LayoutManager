import sublime
import sublime_plugin

class LayoutManagerCommand( sublime_plugin.WindowCommand ):

    layouts = [
        # 0
        {
            "cols": [0.0, 1.0],
            "rows": [0.0, 1.0],
            "cells": [[0, 0, 1, 1]]
        },
        # Vertical Layouts
        # 1
        {
            "cols": [0.0, 0.5, 1.0],
            "rows": [0.0, 1.0],
            "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
        },
        # 2
        {
            "cols": [0.0, 0.33, 0.66, 1.0],
            "rows": [0.0, 1.0],
            "cells": [[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1]]
        },
        # 3
        {
            "cols": [0.0, 0.25, 0.5, 0.75, 1.0],
            "rows": [0.0, 1.0],
            "cells": [[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1], [3, 0, 4, 1]]
        },
        # Grid Layouts
        # ================
        # 4
        {
            "cols": [0.0, 0.5, 1.0],
            "rows": [0.0, 0.5, 1.0],
            "cells":
            [
                [0, 0, 1, 1], [1, 0, 2, 1],
                [0, 1, 1, 2], [1, 1, 2, 2]
            ]
        },
        # Horizontal Layouts
        # ==================
        # 5
        {
            "cols": [0.0, 1.0],
            "rows": [0.0, 0.5, 1.0],
            "cells": [[0, 0, 1, 1], [0, 1, 1, 2]]
        },
        # 6
        {
            "cols": [0.0, 1.0],
            "rows": [0.0, 0.33, 0.66, 1.0],
            "cells": [[0, 0, 1, 1], [0, 1, 1, 2], [0, 2, 1, 3]]
        }
    ]

    def run(self, group):
        current_group = self.window.active_group()

        # horizontal layout (<4)
        if group < 4:
            where_to = group
        # Grid layout
        elif group is 4:
            where_to = 1
        # vertical layout
        elif group > 4:
            where_to = group - 4

        # Create New Layout if it doesn't exist
        if self.window.num_groups() < group+1:
            self.set_layout(group, current_group)

        self.window.run_command("move_to_group", {"group": where_to})
        sublime.set_timeout_async(lambda: self.focus(where_to), 200)


    def focus(self, group):
        self.window.focus_group(group)


    def set_layout(self, group, from_group):
        self.window.run_command("set_layout", self.layouts[group])
        self.focus(from_group)

