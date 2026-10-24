"""Chain Theory feature; attributed claims, not independent validation."""
SPEC = {'issue': {'date': '2026-10-24',
           'slug': 'feature-chain-theory',
           'title': 'Chain Theory',
           'url': 'https://theinnermostloop.substack.com/p/chain-theory',
           'thesis': 'Wissner-Gross proposes rebuilding fundamental physics from finite quantum information '
                     'and presents a candidate fine-structure constant as an initial test.',
           'body': '# Chain Theory\n'
                   '\n'
                   'This feature announces Dr. Alex Wissner-Gross’s proposed reconstruction of physics from '
                   'finite quantum-information networks. Its central numerical claim is an algebraic '
                   'candidate for the fine-structure constant, with a separate conjecture connecting the '
                   'mathematical result to the physical measurement.\n'
                   '\n'
                   'This independent, non-endorsed index summarizes the original article and links its '
                   'references. It does not validate the theory, audit the linked proof, or establish '
                   'experimental confirmation. The author explicitly describes parts of the program as '
                   'conditional or underdeveloped. Here the same person occupies two distinct roles: '
                   'newsletter author and researcher making the claims.\n'
                   '\n'
                   '## Reported claims and arguments\n'
                   '\n'
                   '* [Wissner-Gross announces Chain Theory](/developments/2026-10-24-chain-program.md)\n'
                   '* [The feature argues for deriving constants from new '
                   'foundations](/developments/2026-10-24-chain-motivation.md)\n'
                   '* [Finite information bounds motivate discrete '
                   'constituents](/developments/2026-10-24-chain-finite-information.md)\n'
                   '* [A qutrit–qubit pair is proposed to recover gauge '
                   'symmetry](/developments/2026-10-24-chain-gauge-group.md)\n'
                   '* [Undistillable correlations are proposed as hidden particle '
                   'structure](/developments/2026-10-24-chain-unresolved-structure.md)\n'
                   '* [The proposed constituents form a finite entanglement '
                   'network](/developments/2026-10-24-chain-network.md)\n'
                   '* [Chain Theory starts from one finite-network '
                   'axiom](/developments/2026-10-24-chain-axiom.md)\n'
                   '* [The theory proposes an exact candidate for '
                   'alpha](/developments/2026-10-24-chain-alpha-candidate.md)\n'
                   '* [The candidate is compared with CODATA '
                   '2022](/developments/2026-10-24-chain-codata-comparison.md)\n'
                   '* [More precise measurements could test the proposed '
                   'value](/developments/2026-10-24-chain-future-tests.md)\n'
                   '* [A working draft proposes broader physics '
                   'derivations](/developments/2026-10-24-chain-preliminary-results.md)\n'
                   '* [The author supplies a Lean proof and distinguishes '
                   'conjecture](/developments/2026-10-24-chain-formalization.md)\n'
                   '* [Pair dimensions are assigned to six physics '
                   'sectors](/developments/2026-10-24-chain-sector-mapping.md)\n'
                   '* [A dimensional threshold separates proposed observation '
                   'modes](/developments/2026-10-24-chain-distillation-threshold.md)'},
 'developments': [{'id': '2026-10-24-chain-program',
                   'title': 'Wissner-Gross announces Chain Theory',
                   'claim': 'Wissner-Gross announces a research program seeking to reconstruct fundamental '
                            'physics from finite quantum systems and derive constants without fitted '
                            'parameters.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://alexwg.org/publications/ChainTheoryAlpha.pdf',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://alexwg.org/publications/ChainTheoryCompendium.pdf',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://alexwg.org/publications/ChainAlpha.lean',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://alexwg.org/publications/ChainTheoryTalk.pdf',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'description': 'The author presents a new starting point for derivation, while '
                                  'acknowledging that much of the program remains conditional.'},
                  {'id': '2026-10-24-chain-motivation',
                   'title': 'The feature argues for deriving constants from new foundations',
                   'claim': 'Wissner-Gross argues that the long interval without new fundamental structure '
                            'motivates changing physics’ foundations while retaining derivation of constants '
                            'as a goal; this is the author’s assessment of the field.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://en.wikipedia.org/wiki/Planck%27s_law',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Dirac_equation',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Special_relativity',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/General_relativity',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Bohr_model',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/History_of_quantum_mechanics',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Standard_Model',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/W_and_Z_bosons',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Top_quark',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Higgs_boson',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/First_observation_of_gravitational_waves',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Neutrino_oscillation',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Accelerating_expansion_of_the_universe',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Anthropic_principle',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://doi.org/10.1103/PhysRevLett.59.2607',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Cosmological_constant',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/String_theory_landscape',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Copernican_principle',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Swampland_%28physics%29',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-program']},
                  {'id': '2026-10-24-chain-finite-information',
                   'title': 'Finite information bounds motivate discrete constituents',
                   'claim': 'Wissner-Gross interprets information bounds and entanglement-based gravity '
                            'arguments as reasons to start with finitely many finite-dimensional quantum '
                            'systems rather than continuous fields or strings.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://en.wikipedia.org/wiki/Bekenstein_bound',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://doi.org/10.1103/PhysRevD.23.287',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Black_hole_thermodynamics',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://doi.org/10.1103/PhysRevLett.75.1260',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-axiom']},
                  {'id': '2026-10-24-chain-gauge-group',
                   'title': 'A qutrit–qubit pair is proposed to recover gauge symmetry',
                   'claim': 'Wissner-Gross reports that local basis transformations of an entangled '
                            'qutrit–qubit pair recover the Standard Model gauge group, including its '
                            'permitted Z6 quotient; the index does not independently establish this '
                            'derivation.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://en.wikipedia.org/wiki/Grand_Unified_Theory',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://arxiv.org/abs/0904.1556',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Georgi%E2%80%93Glashow_model',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://doi.org/10.1103/PhysRevLett.32.438',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/SO%2810%29',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Proton_decay',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Superpartner',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://alexwg.org/publications/ChainTheoryCompendium.pdf',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-program']},
                  {'id': '2026-10-24-chain-unresolved-structure',
                   'title': 'Undistillable correlations are proposed as hidden particle structure',
                   'claim': 'Wissner-Gross suggests that correlations inaccessible to available distillation '
                            'operations could explain pointlike particle observations while remaining '
                            'indirectly detectable with suitable witnesses.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://en.wikipedia.org/wiki/Elementary_particle',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/History_of_the_periodic_table',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Quark_model',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Preon',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/LOCC',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Entanglement_distillation',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Bound_entanglement',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://doi.org/10.1103/PhysRevLett.80.5239',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Entanglement_witness',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-axiom']},
                  {'id': '2026-10-24-chain-network',
                   'title': 'The proposed constituents form a finite entanglement network',
                   'claim': 'Wissner-Gross describes networks of maximally entangled pairs joined through '
                            'matched bases of separate subsystem copies, invoking entanglement monogamy and '
                            'a tensor-network analogy.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://doi.org/10.3389/fphy.2020.589504',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Schmidt_decomposition',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Monogamy_of_entanglement',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://arxiv.org/abs/cond-mat/0407066',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Tensor_network',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-axiom']},
                  {'id': '2026-10-24-chain-axiom',
                   'title': 'Chain Theory starts from one finite-network axiom',
                   'claim': 'Wissner-Gross posits a finite collection of maximally entangled '
                            'finite-dimensional pairs with shared joins, where knowledge is acquired through '
                            'single-step distillation within the network.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://philpapers.org/archive/WHEIPQ.pdf',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Quantum_network',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://alexwg.org/publications/ChainTheoryCompendium.pdf',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-program']},
                  {'id': '2026-10-24-chain-alpha-candidate',
                   'title': 'The theory proposes an exact candidate for alpha',
                   'claim': 'Wissner-Gross reports the expression (79 + 48√2 + 42√3 + 3√6)/31104 from a '
                            'weighted count of 172 measurement records and conjectures that it equals the '
                            'Thomson-limit fine-structure constant.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://en.wikipedia.org/wiki/Fine-structure_constant',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://www.goodreads.com/quotes/1016482-there-is-a-most-profound-and-beautiful-question-associated-with',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Koide_formula',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://alexwg.org/publications/ChainTheoryAlpha.pdf',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'score': 'inverse: 137.035999189566…; 172 measurement records',
                   'description': 'The article separates a claimed mathematical derivation from the '
                                  'conjectured identification of its result with a physical constant.',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-gauge-group',
                                 'https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-formalization']},
                  {'id': '2026-10-24-chain-codata-comparison',
                   'title': 'The candidate is compared with CODATA 2022',
                   'claim': 'Wissner-Gross reports agreement with the CODATA 2022 recommended inverse '
                            'fine-structure constant through ten significant digits and a separation of 0.60 '
                            'standard deviations, while noting disagreement among experimental '
                            'determinations.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://alexwg.org/publications/ChainTheoryAlpha.pdf',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Committee_on_Data_of_the_International_Science_Council',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://doi.org/10.1103/RevModPhys.97.025002',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'score': 'ten significant digits; 0.60 standard deviations',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-alpha-candidate']},
                  {'id': '2026-10-24-chain-future-tests',
                   'title': 'More precise measurements could test the proposed value',
                   'claim': 'Wissner-Gross points to electron magnetic-moment and atomic-recoil measurements '
                            'aiming for up to tenfold precision improvements as prospective tests that could '
                            'support or rule out the fixed candidate if they converge.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://doi.org/10.1103/PhysRevLett.130.071801',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://doi.org/10.1126/science.aap7706',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://doi.org/10.1038/s41586-020-2964-7',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'score': 'up to ten times more precise',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-codata-comparison']},
                  {'id': '2026-10-24-chain-preliminary-results',
                   'title': 'A working draft proposes broader physics derivations',
                   'claim': 'Wissner-Gross reports preliminary results concerning the gauge group, Born '
                            'rule, Lorentz symmetry, spacetime signature, matter generations, confinement, '
                            'curvature and the cosmological term, with remaining conditions identified in '
                            'the draft.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://alexwg.org/publications/ChainTheoryCompendium.pdf',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-program']},
                  {'id': '2026-10-24-chain-formalization',
                   'title': 'The author supplies a Lean proof and distinguishes conjecture',
                   'claim': 'Wissner-Gross links a Lean proof and describes the algebraic result as '
                            'following from an axiom, definitions and stated interpretations, while '
                            'reserving the identification with alpha as a conjecture; the index has not '
                            'executed or audited that proof.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://arxiv.org/abs/hep-th/0603022',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://arxiv.org/abs/1806.09450',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://doi.org/10.1140/epjc/s10052-018-5844-7',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Noncommutative_standard_model',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Fine-structure_constant#Numerological_explanations',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Lean_%28proof_assistant%29',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://alexwg.org/publications/ChainAlpha.lean',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://alexwg.org/publications/ChainTheoryTalk.pdf',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-alpha-candidate']},
                  {'id': '2026-10-24-chain-sector-mapping',
                   'title': 'Pair dimensions are assigned to six physics sectors',
                   'claim': 'Wissner-Gross assigns pair dimensions (2,2), (3,2), (3,3), (4,2), (4,3) and '
                            '(4,4) respectively to spacetime, electromagnetism, strong, weak, Yukawa and '
                            'Higgs sectors within the proposed framework.',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://en.wikipedia.org/wiki/Spacetime',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Electromagnetism',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Strong_interaction',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Weak_interaction',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Yukawa_interaction',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Higgs_mechanism',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://alexwg.org/publications/ChainTheoryCompendium.pdf',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-axiom']},
                  {'id': '2026-10-24-chain-distillation-threshold',
                   'title': 'A dimensional threshold separates proposed observation modes',
                   'claim': 'Wissner-Gross uses cited mathematical results to argue that direct observation '
                            'by the theory’s distillation operation is available when endpoint dimensions '
                            'multiply to at most six; other proposed sectors require second-order access, '
                            'interpreted as confinement for (3,3).',
                   'domain': 'science',
                   'actor': ['people/alex-wissner-gross'],
                   'author': [{'type': 'Person',
                               'id': 'https://nicholsn.github.io/innermost-loop-kb/people/alex-wissner-gross',
                               'name': 'Dr. Alex Wissner-Gross'}],
                   'tags': ['quantum-information', 'research-claim', 'feature'],
                   'sources': [{'resource': 'https://doi.org/10.1007/BF02391860',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://doi.org/10.1016/0034-4877%2876%2990038-0',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://doi.org/10.1016/0024-3795%2875%2990058-0',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://en.wikipedia.org/wiki/Peres%E2%80%93Horodecki_criterion',
                                'title': 'Reference linked by the Chain Theory feature'},
                               {'resource': 'https://alexwg.org/publications/ChainTheoryCompendium.pdf',
                                'title': 'Reference linked by the Chain Theory feature'}],
                   'body': 'This record summarizes the author’s own research announcement. His reporter role '
                           'is recorded in author and his research role in actor. The proposed derivations '
                           'and physical interpretations have not been independently verified by this index.',
                   'score': 'dimension product at most six',
                   'relatedTo': ['https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-sector-mapping',
                                 'https://nicholsn.github.io/innermost-loop-kb/developments/2026-10-24-chain-unresolved-structure']}]}
