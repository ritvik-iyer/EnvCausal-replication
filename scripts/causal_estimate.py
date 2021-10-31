import dowhy
import econml

def ate_estimate(treatment, data, outcome, causal_graph):
    inspect_datasets = True
    inspect_models = True
    inspect_identified_estimands = True
    inspect_estimates = True
    inspect_refutations = True
    dowhy.causal_refuter.CausalRefuter.DEFAULT_NUM_SIMULATIONS = 100
    dataset = data
    causal_graph = causal_graph
    model = dowhy.CausalModel(data = dataset,
                        treatment = treatment,
                        outcome = outcome,
                        graph = causal_graph.replace("\n", " "))
    # print("####### Model #############################################################################################")
    # print("Common Causes:",model._common_causes)
    # print("Effect Modifiers:",model._effect_modifiers)
    # print("Instruments:",model._instruments)
    # print("Outcome:",model._outcome)
    # print("Treatment:",model._treatment)
    # print("#############################################################################################################")
    estimand = model.identify_effect(proceed_when_unidentifiable=True)
    # print("####### Identified Estimand #####################################################################################")
    # print(estimand)
    # print("###################################################################################################################")
    estimate_li = model.estimate_effect(estimand,method_name = "backdoor.linear_regression", method_params = None)
    estimate_forest = model.estimate_effect(estimand,method_name ="backdoor.econml.orf.DMLOrthoForest",
                                            method_params = {"init_params":{"n_jobs":-1},"fit_params":{}})
    #Linear Results
    #print("####### Linear Estimate ################################################################################")
    # print("*** Class Name ***")
    # print(estimate_li.params['estimator_class'])
    # # print("*** Treatment Name ***")
    # print(model._treatment)
    li_estimate = estimate_li.value
    #print(li_estimate)
    #print("########################################################################################################")
    #Forest Results
    #print("####### Forest Estimate#################################################################################")
    # print("*** Class Name ***")
    # print(estimate_forest.params['estimator_class'])
    # print("*** Treatment Name ***")
    # print(model._treatment)
    forest_estimate = estimate_forest.value
     #print(estimate_forest.value)
    #print("########################################################################################################")
    return li_estimate, forest_estimate
