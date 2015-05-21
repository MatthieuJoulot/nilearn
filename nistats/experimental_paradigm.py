# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
from __future__ import with_statement
"""
An experimental protocol is handled as a pandas DataFrame
that includes an 'onset' field.
This yields the onset time of the events in the paradigm. It can also contain:
* a 'name' field that yields the condition identifier.
* a 'duration' field that yields event duration (for so-called block
  paradigms).
* a 'modulation' field that associated a scalar value to each event.

Author: Bertrand Thirion, 2015
"""

import numpy as np


def check_paradigm(paradigm):
    """ test that the DataFrame is describes a valid experimental paradigm
    A DataFrame is considered as valid whenever it has an 'onset' key.

    Parameters
    ----------
    paradigm: pandas DataFrame
              describes a functional paradigm

    Returns
    -------
    name: array of shape (n_events), dtype='s'
           per-event experimental conditions identifier
           Defaults to np.repeat('dummy', len(onsets))
    onset: array of shape (n_events), dtype='f'
           per-event onset time (in seconds)
    duration: array of shape (n_events), dtype='f'
              per-event durantion, (in seconds)
              defaults to zeros(n_events) when no duration is provided
    modulation: array of shape (n_events), dtype='f'
              per-event modulation, (in seconds)
              defaults to ones(n_events) when no duration is provided

    """
    if 'onset' not in paradigm.keys():
        raise ValueError('The provided paradigm has no onset key')

    onset = np.array(paradigm['onset'])
    n_events = len(onset)
    name = np.repeat('dummy', n_events)
    duration = np.zeros(n_events)
    modulation = np.ones(n_events)
    if 'name' in paradigm.keys():
        name = np.array(paradigm['name'])
    if 'duration' in paradigm.keys():
        duration = np.array(paradigm['duration']).astype(np.float)
    if 'modulation' in paradigm.keys():
        modulation = np.array(paradigm['modulation']).astype(np.float)
    return name, onset, duration, modulation
