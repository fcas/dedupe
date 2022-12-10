from simplecosine.cosine import CosineSetSimilarity

from dedupe import predicates
from dedupe._typing import VariableDefinition
from dedupe.hookspecs import hookimpl
from dedupe.variables.base import FieldType


class SetType(FieldType):
    type = "Set"

    _predicate_functions = (
        predicates.wholeSetPredicate,
        predicates.commonSetElementPredicate,
        predicates.lastSetElementPredicate,
        predicates.commonTwoElementsPredicate,
        predicates.commonThreeElementsPredicate,
        predicates.magnitudeOfCardinality,
        predicates.firstSetElementPredicate,
    )

    _index_predicates = (
        predicates.TfidfSetSearchPredicate,
        predicates.TfidfSetCanopyPredicate,
    )
    _index_thresholds = (0.2, 0.4, 0.6, 0.8)

    def __init__(self, definition: VariableDefinition):
        super(SetType, self).__init__(definition)

        if "corpus" not in definition:
            definition["corpus"] = []

        self.comparator = CosineSetSimilarity(definition["corpus"])  # type: ignore[assignment]


@hookimpl
def register_variable():
    return {SetType.type: SetType}
