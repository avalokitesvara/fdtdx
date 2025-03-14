"""Constraint modules for enforcing physical and fabrication requirements.

This package provides constraint modules that can be applied during optimization
to ensure designs meet physical realizability and fabrication requirements.
Key constraints include:

- Minimum feature size constraints
- Binary material constraints (air/dielectric only)
- Connectivity constraints (no floating material)
- Fabrication constraints (no trapped air, etc.)

The constraints are implemented as modules that can be chained together
and applied during the optimization process.
"""

from .discrete import (
    BinaryMedianFilterModule,
    BrushConstraint2D,
    ConnectHolesAndStructures,
    RemoveFloatingMaterial,
)
from .module import (
    ClosestIndex,
    ContinuousPermittivityTransition,
    IndicesToInversePermittivities,
    StandardToCustomRange,
    StandardToInversePermittivityRange,
    StandardToPlusOneMinusOneRange,
)
from .pillars import PillarMapping

__all__ = [
    "RemoveFloatingMaterial",
    "ConnectHolesAndStructures",
    "BrushConstraint2D",
    "BinaryMedianFilterModule",
    "StandardToInversePermittivityRange",
    "StandardToCustomRange",
    "StandardToPlusOneMinusOneRange",
    "ClosestIndex",
    "IndicesToInversePermittivities",
    "ContinuousPermittivityTransition",
    "PillarMapping",
]
