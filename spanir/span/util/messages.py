#!/usr/bin/env python3

# MIT License
# Copyright (c) 2019 Anshuman Dhuliya

"""Project wide messages.."""

CONTROL_HERE_ERROR = "Control should not reach here."
START_BB_ID_NOT_1 = "Start BB id is not 1 in the given input Dict[BasicBlockId, BB]."
END_BB_ID_NOT_MINUS_1 = (
  "End BB id is not -1 in the given input Dict[BasicBlockId, BB]."
  " This is required if BB count is greater than one."
)

PTR_INDLEV_INVALID = "Indirection level of pointer is less than 1!"
TOP_BOT_BOTH = "You are saying its Top and Bot at the same time!"