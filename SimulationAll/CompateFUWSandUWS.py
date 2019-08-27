import time

from FUWSeq.FUWSequence import FUWSequence
from Parameters.Variable import Variable
from Parameters.FileInfo import FileInfo
from Parameters.userDefined import UserDefined
from UWSeq.UWSequence import UWSequence
from UtilityTechniques.WAMCalculation import WAMCalculation
from UtilityTechniques.DataPreProcessing import PreProcess
# from FUWSeq.FUWSeq import FUWSeq
from UtilityTechniques.ProbabilityWeightAssign import WeightAssign
from Parameters.ProgramVariable import ProgramVariable
from DynamicTrie.Trie import Trie

if __name__ == '__main__':

    # Edit the following lists

    min_sup_lst = [0.25, 0.3]
    wgt_fct_lst = [0.8, 1, 1.2]
    mu_lst = [0.6, 0.7, 0.8]
    # initialize user given parameters
    # UserDefined.min_sup = 0.25
    # UserDefined.wgt_factor = 0.8
    # Variable.mu = .75

    # initialize file info
    prefix = '../Files/SIGN50'
    FileInfo.initial_dataset = open(prefix + '/SIGN_sp.txt', 'r')
    FileInfo.fs = open(prefix + '/initialFS.txt', 'w')
    FileInfo.sfs = open(prefix + '/initialSFS.txt', 'w')

    # Edit Done ...............

    # Dataset Preprocessing
    PreProcess().doProcess()
    # for seq in ProgramVariable.pSDB:
    #     print(seq, ' Print at Nothing')

    print('Preprocess Done!')

    # Weight Assigning
    WeightAssign.assign(ProgramVariable.itemList)
    # WeightAssign.manual_assign()
    print('Weight Assign Done')

    #WAM calculation && DataBase size update
    WAMCalculation.update_WAM()

    Variable.size_of_dataset = len(ProgramVariable.uSDB)
    print(Variable.size_of_dataset, ' size of dataset')
    print('WAM Done')
    for mn_sup in min_sup_lst:
        UserDefined.min_sup = mn_sup
        for fct in wgt_fct_lst:
            UserDefined.wgt_factor = fct
            for mu in mu_lst:
                Variable.mu = mu

                start_time = time.time()
                root_node, total_candidates = FUWSequence().douWSequence()
                fssfs_trie = Trie(root_node)
                fssfs_trie.update_trie(fssfs_trie.root_node)
                total_patterns = fssfs_trie.trie_into_file(fssfs_trie.root_node, '')


                # FileInfo.fs.close()
                # FileInfo.sfs.close()
                end_time = time.time()

                print('FUWS: Total Candidates - ', total_candidates)
                print('FUWS: Total Patterns - ', total_patterns)
                print(start_time, end_time, end_time-start_time)

                start_time = time.time()
                root_node, total_candidates = UWSequence().douWSequence()
                fssfs_trie = Trie(root_node)
                fssfs_trie.update_trie(fssfs_trie.root_node)
                total_patterns = fssfs_trie.trie_into_file(fssfs_trie.root_node, '')
                end_time = time.time()

                print('UWS: Total Candidates - ', total_candidates)
                print('UWS: Total Patterns - ', total_patterns)
                print(start_time, end_time, end_time - start_time)

