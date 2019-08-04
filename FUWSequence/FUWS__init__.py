import time

from Parameters.Variable import Variable
from Parameters.FileInfo import FileInfo
from Parameters.userDefined import UserDefined
from UtilityTechniques.WAMCalculation import WAMCalculation
from UtilityTechniques.DataPreProcessing import PreProcess
from FUWSequence.UWSequence import UWSequence
from UtilityTechniques.ProbabilityWeightAssign import WeightAssign
from Parameters.ProgramVariable import ProgramVariable
from DynamicTrie.Trie import Trie

if __name__ == '__main__':

    # initialize user given parameters
    UserDefined.min_sup = 0.2
    UserDefined.wgt_factor = 0.8
    Variable.mu = 0.5

    # initialize file info
    FileInfo.initial_dataset = open('../LEVIATHAN/LEVIATHAN_sp.txt', 'r')
    FileInfo.fs = open('../Files/initialFS2.csv', 'w')
    FileInfo.sfs = open('../Files/initialSFS.txt', 'w')

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
    start_time = time.time()
    root_node = UWSequence().douWSequence()
    fssfs_trie = Trie(root_node)
    fssfs_trie.update_trie(fssfs_trie.root_node)
    fssfs_trie.trie_into_file(fssfs_trie.root_node, '')

    FileInfo.fs.close()
    FileInfo.sfs.close()
    end_time = time.time()

    print(start_time, end_time, end_time-start_time)



