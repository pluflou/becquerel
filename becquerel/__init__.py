"""Becquerel: Tools for radiation spectral analysis."""

from . import core
from . import parsers
from . import tools
from .__metadata__ import __description__, __url__
from .__metadata__ import __version__, __license__, __copyright__

from .core.rebin import rebin
from .core.spectrum import Spectrum, SpectrumError, UncalibratedError
from .core.energycal import LinearEnergyCal, EnergyCalError, BadInput
from .core.utils import UncertaintiesError
from .core.plotting import SpectrumPlotter, PlottingError

__all__ = ['core', 'parsers', 'tools', 'rebin'
           'Spectrum', 'SpectrumError', 'SpectrumPlotter', 'PlottingError',
           'UncalibratedError', 'LinearEnergyCal', 'EnergyCalError',
           'BadInput', 'UncertaintiesError',
           '__description__', '__url__', '__version__', '__license__',
           '__copyright__']
