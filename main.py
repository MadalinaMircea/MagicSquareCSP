# # # from Backtracking import Backtracking
# # from Solutions.CSPBacktracking import CSPBacktracking
# # from Solutions.CSPBacktrackingWithReferences import CSPBacktrackingWithReferences
# # # from Solutions.CSPRemoveNeighbours import CSPRemoveNeighbours
# # from Solutions.CSPMatrix import CSPMatrix
# #
# # # back = Backtracking(4)
# # back = CSPMatrix(3)
# #
# # for s in back.back(10):
# #     print(str(s))
#
# # from Statistics.Statistics import compare_solutions
# # compare_solutions(4)
#
# from Solutions.CSPBacktracking import CSPBacktracking
# from Solutions.CSPBacktrackingWithReferences import CSPBacktrackingWithReferences
# from Solutions.CSPMatrix import CSPMatrix
# from Utils.Utils import plot_graph
#
# from Statistics.Statistics import plot_graph_comparisons, plot_time_comparisons
#
# print("Hello!")
# option = input("'1'-Plot search graph comparisons\n'2'-Plot time comparisons for one solution\n"
#                "'3'-Plot time comparisons for 2 solutions\n'4'-Compute now\nOption: ")
# optiont = option.strip()
# if optiont == "1":
#     plot_graph_comparisons()
# elif optiont == "2":
#     plot_time_comparisons(0)
# elif optiont == "3":
#     plot_time_comparisons(1)
# elif optiont == "4":
#     try:
#         n = int(input("Give n (ideally <= 4): "))
#
#         sol = input("Choose option:\n\t'1'-CSP Backtracking\n\t"
#                     "'2'-CSP with neighbour references\n\t'3'-CSP matrix\n\t'4'-CSP with limit b'\nOption: ")
#         solt = sol.strip()
#         back = None
#         if solt == "1":
#             back = CSPBacktracking(n)
#         elif solt == "2":
#             back = CSPBacktrackingWithReferences(n)
#         elif solt == "3":
#             back = CSPMatrix(n)
#         elif solt == "4":
#             # back = CSPWithLimit(file)
#             pass
#
#         if back is None:
#             print("Invalid input")
#         else:
#             try:
#                 max_sols = int(input("Give the desired number of solutions: "))
#                 solutions, graph = back.back(max_sols)
#
#                 alive = True
#                 while alive:
#                     opt = input("'1'-Display search graph\n'2'-Search graph stats\n"
#                                 "'3'-Show a solution\n'0'-Exit\nOption: ")
#                     optt = opt.strip()
#                     if optt == "0":
#                         alive = False
#                     elif optt == "1":
#                         try:
#                             plot_graph(graph)
#                         except Exception as e:
#                             print(e)
#                             print("Error plotting graph")
#                     elif optt == "2":
#                         print(str(graph.number_of_nodes()) + " States")
#                     elif optt == "3":
#                         sols = "Choose solution:\n"
#                         for i in range(len(solutions)):
#                             sols = sols + str(i) + '\n'
#                         sols += "Solution number: "
#                         try:
#                             i = int(input(sols))
#                             print(str(solutions[i]))
#                         except Exception as e:
#                             print(e)
#                             print("Invalid input")
#             except Exception as e:
#                 print(e)
#                 print("Invalid input")
#     except:
#         print("Invalid input")
#
# print("Goodbye!")

from Solutions.CSPWithSum import CSPWithSum

back = CSPWithSum(3)
sols, graph = back.back(2)

for s in sols:
    print(str(s))