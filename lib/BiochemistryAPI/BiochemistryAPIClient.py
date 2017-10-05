# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class BiochemistryAPI(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def get_reactions(self, params, context=None):
        """
        Returns data for the requested reactions
        :param params: instance of type "get_reactions_params" (Input
           parameters for the "get_reactions" function. list<reaction_id>
           reactions - a list of the reaction IDs for the reactions to be
           returned (a required argument)) -> structure: parameter
           "reactions" of list of type "reaction_id" (A string identifier
           used for a reaction in a KBase biochemistry.)
        :returns: instance of list of type "Reaction" (Data structures for
           media formulation reaction_id id - ID of reaction string name -
           primary name of reaction string abbrev - abbreviated name of
           reaction list<string> enzymes - list of EC numbers for reaction
           string direction - directionality of reaction string reversibility
           - reversibility of reaction float deltaG - estimated delta G of
           reaction float deltaGErr - uncertainty in estimated delta G of
           reaction string equation - reaction equation in terms of compound
           IDs string definition - reaction equation in terms of compound
           names) -> structure: parameter "id" of type "reaction_id" (A
           string identifier used for a reaction in a KBase biochemistry.),
           parameter "name" of String, parameter "abbrev" of String,
           parameter "enzymes" of list of String, parameter "direction" of
           String, parameter "reversibility" of String, parameter "deltaG" of
           Double, parameter "deltaGErr" of Double, parameter "equation" of
           String, parameter "definition" of String
        """
        return self._client.call_method(
            'BiochemistryAPI.get_reactions',
            [params], self._service_ver, context)

    def get_compounds(self, params, context=None):
        """
        Returns data for the requested compounds
        :param params: instance of type "get_compounds_params" (Input
           parameters for the "get_compounds" function. list<compound_id>
           compounds - a list of the compound IDs for the compounds to be
           returned (a required argument)) -> structure: parameter
           "compounds" of list of type "compound_id" (An identifier for
           compounds in the KBase biochemistry database. e.g. cpd00001)
        :returns: instance of list of type "Compound" (Data structures for
           media formulation compound_id id - ID of compound string abbrev -
           abbreviated name of compound string name - primary name of
           compound list<string> aliases - list of aliases for compound float
           charge - molecular charge of compound float deltaG - estimated
           compound delta G float deltaGErr - uncertainty in estimated
           compound delta G string formula - molecular formula of compound)
           -> structure: parameter "id" of type "compound_id" (An identifier
           for compounds in the KBase biochemistry database. e.g. cpd00001),
           parameter "abbrev" of String, parameter "name" of String,
           parameter "aliases" of list of String, parameter "charge" of
           Double, parameter "deltaG" of Double, parameter "deltaGErr" of
           Double, parameter "formula" of String
        """
        return self._client.call_method(
            'BiochemistryAPI.get_compounds',
            [params], self._service_ver, context)

    def depict_compounds(self, params, context=None):
        """
        Returns a list of depictions for the compound_structures in SVG format
        :param params: instance of type "depict_compounds_params" ->
           structure: parameter "compound_structures" of list of String
        :returns: instance of list of String
        """
        return self._client.call_method(
            'BiochemistryAPI.depict_compounds',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('BiochemistryAPI.status',
                                        [], self._service_ver, context)
