import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))
        if (isinstance(fact, Fact) and fact not in self.facts):
            print("Asserted fact {!r}".format(fact))
            fact.asserted = True
            self.facts.append(fact)
            return

        if (isinstance(fact, Rule) and fact not in self.rules):
            print("Asserted rule {!r}".format(fact))
            fact.asserted = True
            self.rules.append(fact)
            return

        print("Failed to assert")
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        bindings_list = ListOfBindings()
        if (isinstance(fact, Fact)):
            for f in self.facts:
                b = match(f.statement, fact.statement)
                if (isinstance(b, Bindings)):
                    bindings_list.add_bindings(b, facts_rules=[f])
        
        if (len(bindings_list) == 0):
            return False

        return bindings_list
            
