from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
import grpc

import os
import re
import requests
import json
import struct

os.environ['NO_PROXY'] = '172.16.1.197'

class GRPCConfig:
    _instance = None
    # singleton
    def __init__(self):
        # import proto descriptor
        _descriptor_pool.Default().AddSerializedFile(
            b'\n\x12model_config.proto\x12\tinference\"\x96\x01\n\x10ModelRateLimiter\x12\x37\n\tresources\x18\x01 \x03(\x0b\x32$.inference.ModelRateLimiter.Resource\x12\x10\n\x08priority\x18\x02 \x01(\r\x1a\x37\n\x08Resource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06global\x18\x02 \x01(\x08\x12\r\n\x05\x63ount\x18\x03 \x01(\r\"\x87\x04\n\x12ModelInstanceGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\x04kind\x18\x04 \x01(\x0e\x32\".inference.ModelInstanceGroup.Kind\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x31\n\x0crate_limiter\x18\x06 \x01(\x0b\x32\x1b.inference.ModelRateLimiter\x12\x0c\n\x04gpus\x18\x03 \x03(\x05\x12H\n\x11secondary_devices\x18\x08 \x03(\x0b\x32-.inference.ModelInstanceGroup.SecondaryDevice\x12\x0f\n\x07profile\x18\x05 \x03(\t\x12\x0f\n\x07passive\x18\x07 \x01(\x08\x12\x13\n\x0bhost_policy\x18\t \x01(\t\x1a\x9c\x01\n\x0fSecondaryDevice\x12O\n\x04kind\x18\x01 \x01(\x0e\x32\x41.inference.ModelInstanceGroup.SecondaryDevice.SecondaryDeviceKind\x12\x11\n\tdevice_id\x18\x02 \x01(\x03\"%\n\x13SecondaryDeviceKind\x12\x0e\n\nKIND_NVDLA\x10\x00\"A\n\x04Kind\x12\r\n\tKIND_AUTO\x10\x00\x12\x0c\n\x08KIND_GPU\x10\x01\x12\x0c\n\x08KIND_CPU\x10\x02\x12\x0e\n\nKIND_MODEL\x10\x03\"#\n\x12ModelTensorReshape\x12\r\n\x05shape\x18\x01 \x03(\x03\"\xb2\x02\n\nModelInput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\tdata_type\x18\x02 \x01(\x0e\x32\x13.inference.DataType\x12,\n\x06\x66ormat\x18\x03 \x01(\x0e\x32\x1c.inference.ModelInput.Format\x12\x0c\n\x04\x64ims\x18\x04 \x03(\x03\x12.\n\x07reshape\x18\x05 \x01(\x0b\x32\x1d.inference.ModelTensorReshape\x12\x17\n\x0fis_shape_tensor\x18\x06 \x01(\x08\x12\x1a\n\x12\x61llow_ragged_batch\x18\x07 \x01(\x08\x12\x10\n\x08optional\x18\x08 \x01(\x08\";\n\x06\x46ormat\x12\x0f\n\x0b\x46ORMAT_NONE\x10\x00\x12\x0f\n\x0b\x46ORMAT_NHWC\x10\x01\x12\x0f\n\x0b\x46ORMAT_NCHW\x10\x02\"\xb2\x01\n\x0bModelOutput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\tdata_type\x18\x02 \x01(\x0e\x32\x13.inference.DataType\x12\x0c\n\x04\x64ims\x18\x03 \x03(\x03\x12.\n\x07reshape\x18\x05 \x01(\x0b\x32\x1d.inference.ModelTensorReshape\x12\x16\n\x0elabel_filename\x18\x04 \x01(\t\x12\x17\n\x0fis_shape_tensor\x18\x06 \x01(\x08\"\xd9\x02\n\nBatchInput\x12(\n\x04kind\x18\x01 \x01(\x0e\x32\x1a.inference.BatchInput.Kind\x12\x13\n\x0btarget_name\x18\x02 \x03(\t\x12&\n\tdata_type\x18\x03 \x01(\x0e\x32\x13.inference.DataType\x12\x14\n\x0csource_input\x18\x04 \x03(\t\"\xcd\x01\n\x04Kind\x12\x17\n\x13\x42\x41TCH_ELEMENT_COUNT\x10\x00\x12#\n\x1f\x42\x41TCH_ACCUMULATED_ELEMENT_COUNT\x10\x01\x12-\n)BATCH_ACCUMULATED_ELEMENT_COUNT_WITH_ZERO\x10\x02\x12$\n BATCH_MAX_ELEMENT_COUNT_AS_SHAPE\x10\x03\x12\x14\n\x10\x42\x41TCH_ITEM_SHAPE\x10\x04\x12\x1c\n\x18\x42\x41TCH_ITEM_SHAPE_FLATTEN\x10\x05\"\x8f\x01\n\x0b\x42\x61tchOutput\x12\x13\n\x0btarget_name\x18\x01 \x03(\t\x12)\n\x04kind\x18\x02 \x01(\x0e\x32\x1b.inference.BatchOutput.Kind\x12\x14\n\x0csource_input\x18\x03 \x03(\t\"*\n\x04Kind\x12\"\n\x1e\x42\x41TCH_SCATTER_WITH_INPUT_SHAPE\x10\x00\"\x90\x02\n\x12ModelVersionPolicy\x12\x36\n\x06latest\x18\x01 \x01(\x0b\x32$.inference.ModelVersionPolicy.LatestH\x00\x12\x30\n\x03\x61ll\x18\x02 \x01(\x0b\x32!.inference.ModelVersionPolicy.AllH\x00\x12:\n\x08specific\x18\x03 \x01(\x0b\x32&.inference.ModelVersionPolicy.SpecificH\x00\x1a\x1e\n\x06Latest\x12\x14\n\x0cnum_versions\x18\x01 \x01(\r\x1a\x05\n\x03\x41ll\x1a\x1c\n\x08Specific\x12\x10\n\x08versions\x18\x01 \x03(\x03\x42\x0f\n\rpolicy_choice\"\xfd\r\n\x17ModelOptimizationPolicy\x12\x37\n\x05graph\x18\x01 \x01(\x0b\x32(.inference.ModelOptimizationPolicy.Graph\x12\x42\n\x08priority\x18\x02 \x01(\x0e\x32\x30.inference.ModelOptimizationPolicy.ModelPriority\x12\x35\n\x04\x63uda\x18\x03 \x01(\x0b\x32\'.inference.ModelOptimizationPolicy.Cuda\x12X\n\x16\x65xecution_accelerators\x18\x04 \x01(\x0b\x32\x38.inference.ModelOptimizationPolicy.ExecutionAccelerators\x12R\n\x13input_pinned_memory\x18\x05 \x01(\x0b\x32\x35.inference.ModelOptimizationPolicy.PinnedMemoryBuffer\x12S\n\x14output_pinned_memory\x18\x06 \x01(\x0b\x32\x35.inference.ModelOptimizationPolicy.PinnedMemoryBuffer\x12&\n\x1egather_kernel_buffer_threshold\x18\x07 \x01(\r\x12\x16\n\x0e\x65\x61ger_batching\x18\x08 \x01(\x08\x1a\x16\n\x05Graph\x12\r\n\x05level\x18\x01 \x01(\x05\x1a\xba\x05\n\x04\x43uda\x12\x0e\n\x06graphs\x18\x01 \x01(\x08\x12\x18\n\x10\x62usy_wait_events\x18\x02 \x01(\x08\x12\x45\n\ngraph_spec\x18\x03 \x03(\x0b\x32\x31.inference.ModelOptimizationPolicy.Cuda.GraphSpec\x12\x1a\n\x12output_copy_stream\x18\x04 \x01(\x08\x1a\xa4\x04\n\tGraphSpec\x12\x12\n\nbatch_size\x18\x01 \x01(\x05\x12K\n\x05input\x18\x02 \x03(\x0b\x32<.inference.ModelOptimizationPolicy.Cuda.GraphSpec.InputEntry\x12W\n\x11graph_lower_bound\x18\x03 \x01(\x0b\x32<.inference.ModelOptimizationPolicy.Cuda.GraphSpec.LowerBound\x1a\x14\n\x05Shape\x12\x0b\n\x03\x64im\x18\x01 \x03(\x03\x1a\xdf\x01\n\nLowerBound\x12\x12\n\nbatch_size\x18\x01 \x01(\x05\x12V\n\x05input\x18\x02 \x03(\x0b\x32G.inference.ModelOptimizationPolicy.Cuda.GraphSpec.LowerBound.InputEntry\x1a\x65\n\nInputEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x46\n\x05value\x18\x02 \x01(\x0b\x32\x37.inference.ModelOptimizationPolicy.Cuda.GraphSpec.Shape:\x02\x38\x01\x1a\x65\n\nInputEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x46\n\x05value\x18\x02 \x01(\x0b\x32\x37.inference.ModelOptimizationPolicy.Cuda.GraphSpec.Shape:\x02\x38\x01\x1a\xa4\x03\n\x15\x45xecutionAccelerators\x12g\n\x19gpu_execution_accelerator\x18\x01 \x03(\x0b\x32\x44.inference.ModelOptimizationPolicy.ExecutionAccelerators.Accelerator\x12g\n\x19\x63pu_execution_accelerator\x18\x02 \x03(\x0b\x32\x44.inference.ModelOptimizationPolicy.ExecutionAccelerators.Accelerator\x1a\xb8\x01\n\x0b\x41\x63\x63\x65lerator\x12\x0c\n\x04name\x18\x01 \x01(\t\x12h\n\nparameters\x18\x02 \x03(\x0b\x32T.inference.ModelOptimizationPolicy.ExecutionAccelerators.Accelerator.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a$\n\x12PinnedMemoryBuffer\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\"I\n\rModelPriority\x12\x14\n\x10PRIORITY_DEFAULT\x10\x00\x12\x10\n\x0cPRIORITY_MAX\x10\x01\x12\x10\n\x0cPRIORITY_MIN\x10\x02\"\xdb\x01\n\x10ModelQueuePolicy\x12\x41\n\x0etimeout_action\x18\x01 \x01(\x0e\x32).inference.ModelQueuePolicy.TimeoutAction\x12$\n\x1c\x64\x65\x66\x61ult_timeout_microseconds\x18\x02 \x01(\x04\x12\x1e\n\x16\x61llow_timeout_override\x18\x03 \x01(\x08\x12\x16\n\x0emax_queue_size\x18\x04 \x01(\r\"&\n\rTimeoutAction\x12\n\n\x06REJECT\x10\x00\x12\t\n\x05\x44\x45LAY\x10\x01\"\x9b\x03\n\x14ModelDynamicBatching\x12\x1c\n\x14preferred_batch_size\x18\x01 \x03(\x05\x12$\n\x1cmax_queue_delay_microseconds\x18\x02 \x01(\x04\x12\x19\n\x11preserve_ordering\x18\x03 \x01(\x08\x12\x17\n\x0fpriority_levels\x18\x04 \x01(\r\x12\x1e\n\x16\x64\x65\x66\x61ult_priority_level\x18\x05 \x01(\r\x12\x39\n\x14\x64\x65\x66\x61ult_queue_policy\x18\x06 \x01(\x0b\x32\x1b.inference.ModelQueuePolicy\x12W\n\x15priority_queue_policy\x18\x07 \x03(\x0b\x32\x38.inference.ModelDynamicBatching.PriorityQueuePolicyEntry\x1aW\n\x18PriorityQueuePolicyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.inference.ModelQueuePolicy:\x02\x38\x01\"\xef\t\n\x15ModelSequenceBatching\x12\x41\n\x06\x64irect\x18\x03 \x01(\x0b\x32/.inference.ModelSequenceBatching.StrategyDirectH\x00\x12\x41\n\x06oldest\x18\x04 \x01(\x0b\x32/.inference.ModelSequenceBatching.StrategyOldestH\x00\x12&\n\x1emax_sequence_idle_microseconds\x18\x01 \x01(\x04\x12\x44\n\rcontrol_input\x18\x02 \x03(\x0b\x32-.inference.ModelSequenceBatching.ControlInput\x12\x35\n\x05state\x18\x05 \x03(\x0b\x32&.inference.ModelSequenceBatching.State\x1a\xb1\x02\n\x07\x43ontrol\x12;\n\x04kind\x18\x01 \x01(\x0e\x32-.inference.ModelSequenceBatching.Control.Kind\x12\x18\n\x10int32_false_true\x18\x02 \x03(\x05\x12\x17\n\x0f\x66p32_false_true\x18\x03 \x03(\x02\x12\x17\n\x0f\x62ool_false_true\x18\x05 \x03(\x08\x12&\n\tdata_type\x18\x04 \x01(\x0e\x32\x13.inference.DataType\"u\n\x04Kind\x12\x1a\n\x16\x43ONTROL_SEQUENCE_START\x10\x00\x12\x1a\n\x16\x43ONTROL_SEQUENCE_READY\x10\x01\x12\x18\n\x14\x43ONTROL_SEQUENCE_END\x10\x02\x12\x1b\n\x17\x43ONTROL_SEQUENCE_CORRID\x10\x03\x1aW\n\x0c\x43ontrolInput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x39\n\x07\x63ontrol\x18\x02 \x03(\x0b\x32(.inference.ModelSequenceBatching.Control\x1a\x8a\x01\n\x0cInitialState\x12&\n\tdata_type\x18\x01 \x01(\x0e\x32\x13.inference.DataType\x12\x0c\n\x04\x64ims\x18\x02 \x03(\x03\x12\x13\n\tzero_data\x18\x03 \x01(\x08H\x00\x12\x13\n\tdata_file\x18\x04 \x01(\tH\x00\x12\x0c\n\x04name\x18\x05 \x01(\tB\x0c\n\nstate_data\x1a\xac\x01\n\x05State\x12\x12\n\ninput_name\x18\x01 \x01(\t\x12\x13\n\x0boutput_name\x18\x02 \x01(\t\x12&\n\tdata_type\x18\x03 \x01(\x0e\x32\x13.inference.DataType\x12\x0c\n\x04\x64ims\x18\x04 \x03(\x03\x12\x44\n\rinitial_state\x18\x05 \x03(\x0b\x32-.inference.ModelSequenceBatching.InitialState\x1aX\n\x0eStrategyDirect\x12$\n\x1cmax_queue_delay_microseconds\x18\x01 \x01(\x04\x12 \n\x18minimum_slot_utilization\x18\x02 \x01(\x02\x1au\n\x0eStrategyOldest\x12\x1f\n\x17max_candidate_sequences\x18\x01 \x01(\x05\x12\x1c\n\x14preferred_batch_size\x18\x02 \x03(\x05\x12$\n\x1cmax_queue_delay_microseconds\x18\x03 \x01(\x04\x42\x11\n\x0fstrategy_choice\"\xdd\x02\n\x0fModelEnsembling\x12-\n\x04step\x18\x01 \x03(\x0b\x32\x1f.inference.ModelEnsembling.Step\x1a\x9a\x02\n\x04Step\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x15\n\rmodel_version\x18\x02 \x01(\x03\x12@\n\tinput_map\x18\x03 \x03(\x0b\x32-.inference.ModelEnsembling.Step.InputMapEntry\x12\x42\n\noutput_map\x18\x04 \x03(\x0b\x32..inference.ModelEnsembling.Step.OutputMapEntry\x1a/\n\rInputMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x30\n\x0eOutputMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"&\n\x0eModelParameter\x12\x14\n\x0cstring_value\x18\x01 \x01(\t\"\xd9\x02\n\x0bModelWarmup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nbatch_size\x18\x02 \x01(\r\x12\x32\n\x06inputs\x18\x03 \x03(\x0b\x32\".inference.ModelWarmup.InputsEntry\x12\r\n\x05\x63ount\x18\x04 \x01(\r\x1a\x97\x01\n\x05Input\x12&\n\tdata_type\x18\x01 \x01(\x0e\x32\x13.inference.DataType\x12\x0c\n\x04\x64ims\x18\x02 \x03(\x03\x12\x13\n\tzero_data\x18\x03 \x01(\x08H\x00\x12\x15\n\x0brandom_data\x18\x04 \x01(\x08H\x00\x12\x19\n\x0finput_data_file\x18\x05 \x01(\tH\x00\x42\x11\n\x0finput_data_type\x1aK\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.inference.ModelWarmup.Input:\x02\x38\x01\".\n\x0fModelOperations\x12\x1b\n\x13op_library_filename\x18\x01 \x03(\t\"+\n\x16ModelTransactionPolicy\x12\x11\n\tdecoupled\x18\x01 \x01(\x08\"\xe6\x01\n\x15ModelRepositoryAgents\x12\x36\n\x06\x61gents\x18\x01 \x03(\x0b\x32&.inference.ModelRepositoryAgents.Agent\x1a\x94\x01\n\x05\x41gent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12J\n\nparameters\x18\x02 \x03(\x0b\x32\x36.inference.ModelRepositoryAgents.Agent.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"$\n\x12ModelResponseCache\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\"\xb2\n\n\x0bModelConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08platform\x18\x02 \x01(\t\x12\x0f\n\x07\x62\x61\x63kend\x18\x11 \x01(\t\x12\x35\n\x0eversion_policy\x18\x03 \x01(\x0b\x32\x1d.inference.ModelVersionPolicy\x12\x16\n\x0emax_batch_size\x18\x04 \x01(\x05\x12$\n\x05input\x18\x05 \x03(\x0b\x32\x15.inference.ModelInput\x12&\n\x06output\x18\x06 \x03(\x0b\x32\x16.inference.ModelOutput\x12*\n\x0b\x62\x61tch_input\x18\x14 \x03(\x0b\x32\x15.inference.BatchInput\x12,\n\x0c\x62\x61tch_output\x18\x15 \x03(\x0b\x32\x16.inference.BatchOutput\x12\x38\n\x0coptimization\x18\x0c \x01(\x0b\x32\".inference.ModelOptimizationPolicy\x12;\n\x10\x64ynamic_batching\x18\x0b \x01(\x0b\x32\x1f.inference.ModelDynamicBatchingH\x00\x12=\n\x11sequence_batching\x18\r \x01(\x0b\x32 .inference.ModelSequenceBatchingH\x00\x12\x39\n\x13\x65nsemble_scheduling\x18\x0f \x01(\x0b\x32\x1a.inference.ModelEnsemblingH\x00\x12\x35\n\x0einstance_group\x18\x07 \x03(\x0b\x32\x1d.inference.ModelInstanceGroup\x12\x1e\n\x16\x64\x65\x66\x61ult_model_filename\x18\x08 \x01(\t\x12H\n\x12\x63\x63_model_filenames\x18\t \x03(\x0b\x32,.inference.ModelConfig.CcModelFilenamesEntry\x12;\n\x0bmetric_tags\x18\n \x03(\x0b\x32&.inference.ModelConfig.MetricTagsEntry\x12:\n\nparameters\x18\x0e \x03(\x0b\x32&.inference.ModelConfig.ParametersEntry\x12,\n\x0cmodel_warmup\x18\x10 \x03(\x0b\x32\x16.inference.ModelWarmup\x12\x34\n\x10model_operations\x18\x12 \x01(\x0b\x32\x1a.inference.ModelOperations\x12\x43\n\x18model_transaction_policy\x18\x13 \x01(\x0b\x32!.inference.ModelTransactionPolicy\x12\x41\n\x17model_repository_agents\x18\x17 \x01(\x0b\x32 .inference.ModelRepositoryAgents\x12\x35\n\x0eresponse_cache\x18\x18 \x01(\x0b\x32\x1d.inference.ModelResponseCache\x1a\x37\n\x15\x43\x63ModelFilenamesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x31\n\x0fMetricTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aL\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.inference.ModelParameter:\x02\x38\x01\x42\x13\n\x11scheduling_choice*\xfa\x01\n\x08\x44\x61taType\x12\x10\n\x0cTYPE_INVALID\x10\x00\x12\r\n\tTYPE_BOOL\x10\x01\x12\x0e\n\nTYPE_UINT8\x10\x02\x12\x0f\n\x0bTYPE_UINT16\x10\x03\x12\x0f\n\x0bTYPE_UINT32\x10\x04\x12\x0f\n\x0bTYPE_UINT64\x10\x05\x12\r\n\tTYPE_INT8\x10\x06\x12\x0e\n\nTYPE_INT16\x10\x07\x12\x0e\n\nTYPE_INT32\x10\x08\x12\x0e\n\nTYPE_INT64\x10\t\x12\r\n\tTYPE_FP16\x10\n\x12\r\n\tTYPE_FP32\x10\x0b\x12\r\n\tTYPE_FP64\x10\x0c\x12\x0f\n\x0bTYPE_STRING\x10\r\x12\r\n\tTYPE_BF16\x10\x0e\x62\x06proto3')
        DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
            b'\n\x12grpc_service.proto\x12\tinference\x1a\x12model_config.proto\"\x13\n\x11ServerLiveRequest\"\"\n\x12ServerLiveResponse\x12\x0c\n\x04live\x18\x01 \x01(\x08\"\x14\n\x12ServerReadyRequest\"$\n\x13ServerReadyResponse\x12\r\n\x05ready\x18\x01 \x01(\x08\"2\n\x11ModelReadyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"#\n\x12ModelReadyResponse\x12\r\n\x05ready\x18\x01 \x01(\x08\"\x17\n\x15ServerMetadataRequest\"K\n\x16ServerMetadataResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x12\n\nextensions\x18\x03 \x03(\t\"5\n\x14ModelMetadataRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\x8d\x02\n\x15ModelMetadataResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08versions\x18\x02 \x03(\t\x12\x10\n\x08platform\x18\x03 \x01(\t\x12?\n\x06inputs\x18\x04 \x03(\x0b\x32/.inference.ModelMetadataResponse.TensorMetadata\x12@\n\x07outputs\x18\x05 \x03(\x0b\x32/.inference.ModelMetadataResponse.TensorMetadata\x1a?\n\x0eTensorMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tatype\x18\x02 \x01(\t\x12\r\n\x05shape\x18\x03 \x03(\x03\"i\n\x0eInferParameter\x12\x14\n\nbool_param\x18\x01 \x01(\x08H\x00\x12\x15\n\x0bint64_param\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cstring_param\x18\x03 \x01(\tH\x00\x42\x12\n\x10parameter_choice\"\xd0\x01\n\x13InferTensorContents\x12\x15\n\rbool_contents\x18\x01 \x03(\x08\x12\x14\n\x0cint_contents\x18\x02 \x03(\x05\x12\x16\n\x0eint64_contents\x18\x03 \x03(\x03\x12\x15\n\ruint_contents\x18\x04 \x03(\r\x12\x17\n\x0fuint64_contents\x18\x05 \x03(\x04\x12\x15\n\rfp32_contents\x18\x06 \x03(\x02\x12\x15\n\rfp64_contents\x18\x07 \x03(\x01\x12\x16\n\x0e\x62ytes_contents\x18\x08 \x03(\x0c\"\xee\x06\n\x11ModelInferRequest\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x15\n\rmodel_version\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12@\n\nparameters\x18\x04 \x03(\x0b\x32,.inference.ModelInferRequest.ParametersEntry\x12=\n\x06inputs\x18\x05 \x03(\x0b\x32-.inference.ModelInferRequest.InferInputTensor\x12H\n\x07outputs\x18\x06 \x03(\x0b\x32\x37.inference.ModelInferRequest.InferRequestedOutputTensor\x12\x1a\n\x12raw_input_contents\x18\x07 \x03(\x0c\x1a\x94\x02\n\x10InferInputTensor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tatype\x18\x02 \x01(\t\x12\r\n\x05shape\x18\x03 \x03(\x03\x12Q\n\nparameters\x18\x04 \x03(\x0b\x32=.inference.ModelInferRequest.InferInputTensor.ParametersEntry\x12\x30\n\x08\x63ontents\x18\x05 \x01(\x0b\x32\x1e.inference.InferTensorContents\x1aL\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.inference.InferParameter:\x02\x38\x01\x1a\xd5\x01\n\x1aInferRequestedOutputTensor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12[\n\nparameters\x18\x02 \x03(\x0b\x32G.inference.ModelInferRequest.InferRequestedOutputTensor.ParametersEntry\x1aL\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.inference.InferParameter:\x02\x38\x01\x1aL\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.inference.InferParameter:\x02\x38\x01\"\xd5\x04\n\x12ModelInferResponse\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x15\n\rmodel_version\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x41\n\nparameters\x18\x04 \x03(\x0b\x32-.inference.ModelInferResponse.ParametersEntry\x12@\n\x07outputs\x18\x05 \x03(\x0b\x32/.inference.ModelInferResponse.InferOutputTensor\x12\x1b\n\x13raw_output_contents\x18\x06 \x03(\x0c\x1a\x97\x02\n\x11InferOutputTensor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tatype\x18\x02 \x01(\t\x12\r\n\x05shape\x18\x03 \x03(\x03\x12S\n\nparameters\x18\x04 \x03(\x0b\x32?.inference.ModelInferResponse.InferOutputTensor.ParametersEntry\x12\x30\n\x08\x63ontents\x18\x05 \x01(\x0b\x32\x1e.inference.InferTensorContents\x1aL\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.inference.InferParameter:\x02\x38\x01\x1aL\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.inference.InferParameter:\x02\x38\x01\"h\n\x18ModelStreamInferResponse\x12\x15\n\rerror_message\x18\x01 \x01(\t\x12\x35\n\x0einfer_response\x18\x02 \x01(\x0b\x32\x1d.inference.ModelInferResponse\"3\n\x12ModelConfigRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"=\n\x13ModelConfigResponse\x12&\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x16.inference.ModelConfig\"7\n\x16ModelStatisticsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\".\n\x11StatisticDuration\x12\r\n\x05\x63ount\x18\x01 \x01(\x04\x12\n\n\x02ns\x18\x02 \x01(\x04\"\x9c\x03\n\x0fInferStatistics\x12-\n\x07success\x18\x01 \x01(\x0b\x32\x1c.inference.StatisticDuration\x12*\n\x04\x66\x61il\x18\x02 \x01(\x0b\x32\x1c.inference.StatisticDuration\x12+\n\x05queue\x18\x03 \x01(\x0b\x32\x1c.inference.StatisticDuration\x12\x33\n\rcompute_input\x18\x04 \x01(\x0b\x32\x1c.inference.StatisticDuration\x12\x33\n\rcompute_infer\x18\x05 \x01(\x0b\x32\x1c.inference.StatisticDuration\x12\x34\n\x0e\x63ompute_output\x18\x06 \x01(\x0b\x32\x1c.inference.StatisticDuration\x12/\n\tcache_hit\x18\x07 \x01(\x0b\x32\x1c.inference.StatisticDuration\x12\x30\n\ncache_miss\x18\x08 \x01(\x0b\x32\x1c.inference.StatisticDuration\"\xca\x01\n\x14InferBatchStatistics\x12\x12\n\nbatch_size\x18\x01 \x01(\x04\x12\x33\n\rcompute_input\x18\x02 \x01(\x0b\x32\x1c.inference.StatisticDuration\x12\x33\n\rcompute_infer\x18\x03 \x01(\x0b\x32\x1c.inference.StatisticDuration\x12\x34\n\x0e\x63ompute_output\x18\x04 \x01(\x0b\x32\x1c.inference.StatisticDuration\"\xe5\x01\n\x0fModelStatistics\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x16\n\x0elast_inference\x18\x03 \x01(\x04\x12\x17\n\x0finference_count\x18\x04 \x01(\x04\x12\x17\n\x0f\x65xecution_count\x18\x05 \x01(\x04\x12\x33\n\x0finference_stats\x18\x06 \x01(\x0b\x32\x1a.inference.InferStatistics\x12\x34\n\x0b\x62\x61tch_stats\x18\x07 \x03(\x0b\x32\x1f.inference.InferBatchStatistics\"J\n\x17ModelStatisticsResponse\x12/\n\x0bmodel_stats\x18\x01 \x03(\x0b\x32\x1a.inference.ModelStatistics\"\x8a\x01\n\x18ModelRepositoryParameter\x12\x14\n\nbool_param\x18\x01 \x01(\x08H\x00\x12\x15\n\x0bint64_param\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cstring_param\x18\x03 \x01(\tH\x00\x12\x15\n\x0b\x62ytes_param\x18\x04 \x01(\x0cH\x00\x42\x12\n\x10parameter_choice\"@\n\x16RepositoryIndexRequest\x12\x17\n\x0frepository_name\x18\x01 \x01(\t\x12\r\n\x05ready\x18\x02 \x01(\x08\"\xa4\x01\n\x17RepositoryIndexResponse\x12=\n\x06models\x18\x01 \x03(\x0b\x32-.inference.RepositoryIndexResponse.ModelIndex\x1aJ\n\nModelIndex\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\"\xec\x01\n\x1aRepositoryModelLoadRequest\x12\x17\n\x0frepository_name\x18\x01 \x01(\t\x12\x12\n\nmodel_name\x18\x02 \x01(\t\x12I\n\nparameters\x18\x03 \x03(\x0b\x32\x35.inference.RepositoryModelLoadRequest.ParametersEntry\x1aV\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32#.inference.ModelRepositoryParameter:\x02\x38\x01\"\x1d\n\x1bRepositoryModelLoadResponse\"\xf0\x01\n\x1cRepositoryModelUnloadRequest\x12\x17\n\x0frepository_name\x18\x01 \x01(\t\x12\x12\n\nmodel_name\x18\x02 \x01(\t\x12K\n\nparameters\x18\x03 \x03(\x0b\x32\x37.inference.RepositoryModelUnloadRequest.ParametersEntry\x1aV\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32#.inference.ModelRepositoryParameter:\x02\x38\x01\"\x1f\n\x1dRepositoryModelUnloadResponse\"/\n\x1fSystemSharedMemoryStatusRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xa5\x02\n SystemSharedMemoryStatusResponse\x12I\n\x07regions\x18\x01 \x03(\x0b\x32\x38.inference.SystemSharedMemoryStatusResponse.RegionsEntry\x1aL\n\x0cRegionStatus\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0e\n\x06offset\x18\x03 \x01(\x04\x12\x11\n\tbyte_size\x18\x04 \x01(\x04\x1ah\n\x0cRegionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x38.inference.SystemSharedMemoryStatusResponse.RegionStatus:\x02\x38\x01\"a\n!SystemSharedMemoryRegisterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0e\n\x06offset\x18\x03 \x01(\x04\x12\x11\n\tbyte_size\x18\x04 \x01(\x04\"$\n\"SystemSharedMemoryRegisterResponse\"3\n#SystemSharedMemoryUnregisterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"&\n$SystemSharedMemoryUnregisterResponse\"-\n\x1d\x43udaSharedMemoryStatusRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x95\x02\n\x1e\x43udaSharedMemoryStatusResponse\x12G\n\x07regions\x18\x01 \x03(\x0b\x32\x36.inference.CudaSharedMemoryStatusResponse.RegionsEntry\x1a\x42\n\x0cRegionStatus\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdevice_id\x18\x02 \x01(\x04\x12\x11\n\tbyte_size\x18\x03 \x01(\x04\x1a\x66\n\x0cRegionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.inference.CudaSharedMemoryStatusResponse.RegionStatus:\x02\x38\x01\"i\n\x1f\x43udaSharedMemoryRegisterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nraw_handle\x18\x02 \x01(\x0c\x12\x11\n\tdevice_id\x18\x03 \x01(\x03\x12\x11\n\tbyte_size\x18\x04 \x01(\x04\"\"\n CudaSharedMemoryRegisterResponse\"1\n!CudaSharedMemoryUnregisterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"$\n\"CudaSharedMemoryUnregisterResponse\"\xe6\x01\n\x13TraceSettingRequest\x12>\n\x08settings\x18\x01 \x03(\x0b\x32,.inference.TraceSettingRequest.SettingsEntry\x12\x12\n\nmodel_name\x18\x02 \x01(\t\x1a\x1d\n\x0cSettingValue\x12\r\n\x05value\x18\x01 \x03(\t\x1a\\\n\rSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b\x32+.inference.TraceSettingRequest.SettingValue:\x02\x38\x01\"\xd5\x01\n\x14TraceSettingResponse\x12?\n\x08settings\x18\x01 \x03(\x0b\x32-.inference.TraceSettingResponse.SettingsEntry\x1a\x1d\n\x0cSettingValue\x12\r\n\x05value\x18\x01 \x03(\t\x1a]\n\rSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.inference.TraceSettingResponse.SettingValue:\x02\x38\x01\"\x9a\x02\n\x12LogSettingsRequest\x12=\n\x08settings\x18\x01 \x03(\x0b\x32+.inference.LogSettingsRequest.SettingsEntry\x1ah\n\x0cSettingValue\x12\x14\n\nbool_param\x18\x01 \x01(\x08H\x00\x12\x16\n\x0cuint32_param\x18\x02 \x01(\rH\x00\x12\x16\n\x0cstring_param\x18\x03 \x01(\tH\x00\x42\x12\n\x10parameter_choice\x1a[\n\rSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.inference.LogSettingsRequest.SettingValue:\x02\x38\x01\"\x9d\x02\n\x13LogSettingsResponse\x12>\n\x08settings\x18\x01 \x03(\x0b\x32,.inference.LogSettingsResponse.SettingsEntry\x1ah\n\x0cSettingValue\x12\x14\n\nbool_param\x18\x01 \x01(\x08H\x00\x12\x16\n\x0cuint32_param\x18\x02 \x01(\rH\x00\x12\x16\n\x0cstring_param\x18\x03 \x01(\tH\x00\x42\x12\n\x10parameter_choice\x1a\\\n\rSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b\x32+.inference.LogSettingsResponse.SettingValue:\x02\x38\x01\x32\xb7\x0f\n\x14GRPCInferenceService\x12K\n\nServerLive\x12\x1c.inference.ServerLiveRequest\x1a\x1d.inference.ServerLiveResponse\"\x00\x12N\n\x0bServerReady\x12\x1d.inference.ServerReadyRequest\x1a\x1e.inference.ServerReadyResponse\"\x00\x12K\n\nModelReady\x12\x1c.inference.ModelReadyRequest\x1a\x1d.inference.ModelReadyResponse\"\x00\x12W\n\x0eServerMetadata\x12 .inference.ServerMetadataRequest\x1a!.inference.ServerMetadataResponse\"\x00\x12T\n\rModelMetadata\x12\x1f.inference.ModelMetadataRequest\x1a .inference.ModelMetadataResponse\"\x00\x12K\n\nModelInfer\x12\x1c.inference.ModelInferRequest\x1a\x1d.inference.ModelInferResponse\"\x00\x12[\n\x10ModelStreamInfer\x12\x1c.inference.ModelInferRequest\x1a#.inference.ModelStreamInferResponse\"\x00(\x01\x30\x01\x12N\n\x0bModelConfig\x12\x1d.inference.ModelConfigRequest\x1a\x1e.inference.ModelConfigResponse\"\x00\x12Z\n\x0fModelStatistics\x12!.inference.ModelStatisticsRequest\x1a\".inference.ModelStatisticsResponse\"\x00\x12Z\n\x0fRepositoryIndex\x12!.inference.RepositoryIndexRequest\x1a\".inference.RepositoryIndexResponse\"\x00\x12\x66\n\x13RepositoryModelLoad\x12%.inference.RepositoryModelLoadRequest\x1a&.inference.RepositoryModelLoadResponse\"\x00\x12l\n\x15RepositoryModelUnload\x12\'.inference.RepositoryModelUnloadRequest\x1a(.inference.RepositoryModelUnloadResponse\"\x00\x12u\n\x18SystemSharedMemoryStatus\x12*.inference.SystemSharedMemoryStatusRequest\x1a+.inference.SystemSharedMemoryStatusResponse\"\x00\x12{\n\x1aSystemSharedMemoryRegister\x12,.inference.SystemSharedMemoryRegisterRequest\x1a-.inference.SystemSharedMemoryRegisterResponse\"\x00\x12\x81\x01\n\x1cSystemSharedMemoryUnregister\x12..inference.SystemSharedMemoryUnregisterRequest\x1a/.inference.SystemSharedMemoryUnregisterResponse\"\x00\x12o\n\x16\x43udaSharedMemoryStatus\x12(.inference.CudaSharedMemoryStatusRequest\x1a).inference.CudaSharedMemoryStatusResponse\"\x00\x12u\n\x18\x43udaSharedMemoryRegister\x12*.inference.CudaSharedMemoryRegisterRequest\x1a+.inference.CudaSharedMemoryRegisterResponse\"\x00\x12{\n\x1a\x43udaSharedMemoryUnregister\x12,.inference.CudaSharedMemoryUnregisterRequest\x1a-.inference.CudaSharedMemoryUnregisterResponse\"\x00\x12Q\n\x0cTraceSetting\x12\x1e.inference.TraceSettingRequest\x1a\x1f.inference.TraceSettingResponse\"\x00\x12N\n\x0bLogSettings\x12\x1d.inference.LogSettingsRequest\x1a\x1e.inference.LogSettingsResponse\"\x00\x62\x06proto3')

        # get request config
        _MODELINFERREQUEST = DESCRIPTOR.message_types_by_name['ModelInferRequest']
        _MODELINFERREQUEST_INFERINPUTTENSOR = _MODELINFERREQUEST.nested_types_by_name['InferInputTensor']
        _MODELINFERREQUEST_INFERINPUTTENSOR_PARAMETERSENTRY = _MODELINFERREQUEST_INFERINPUTTENSOR.nested_types_by_name['ParametersEntry']
        _MODELINFERREQUEST_INFERREQUESTEDOUTPUTTENSOR = _MODELINFERREQUEST.nested_types_by_name['InferRequestedOutputTensor']
        _MODELINFERREQUEST_INFERREQUESTEDOUTPUTTENSOR_PARAMETERSENTRY = \
        _MODELINFERREQUEST_INFERREQUESTEDOUTPUTTENSOR.nested_types_by_name['ParametersEntry']
        _MODELINFERREQUEST_PARAMETERSENTRY = _MODELINFERREQUEST.nested_types_by_name['ParametersEntry']
        # get response config
        _MODELINFERRESPONSE = DESCRIPTOR.message_types_by_name['ModelInferResponse']
        _MODELINFERRESPONSE_INFEROUTPUTTENSOR = _MODELINFERRESPONSE.nested_types_by_name['InferOutputTensor']
        _MODELINFERRESPONSE_INFEROUTPUTTENSOR_PARAMETERSENTRY = \
        _MODELINFERRESPONSE_INFEROUTPUTTENSOR.nested_types_by_name['ParametersEntry']
        _MODELINFERRESPONSE_PARAMETERSENTRY = _MODELINFERRESPONSE.nested_types_by_name['ParametersEntry']

        # request config
        self.ModelInferRequest = _reflection.GeneratedProtocolMessageType('ModelInferRequest', (_message.Message,), {
            'InferInputTensor': _reflection.GeneratedProtocolMessageType('InferInputTensor', (_message.Message,), {
                'ParametersEntry': _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
                    'DESCRIPTOR': _MODELINFERREQUEST_INFERINPUTTENSOR_PARAMETERSENTRY,
                    '__module__': 'grpc_service_pb2'
                }),
                'DESCRIPTOR': _MODELINFERREQUEST_INFERINPUTTENSOR,
                '__module__': 'grpc_service_pb2'
            }),
            'InferRequestedOutputTensor': _reflection.GeneratedProtocolMessageType('InferRequestedOutputTensor',(_message.Message,), {
               'ParametersEntry': _reflection.GeneratedProtocolMessageType(
                   'ParametersEntry',
                   (_message.Message,), {
                       'DESCRIPTOR': _MODELINFERREQUEST_INFERREQUESTEDOUTPUTTENSOR_PARAMETERSENTRY,
                       '__module__': 'grpc_service_pb2'
                   }),
               'DESCRIPTOR': _MODELINFERREQUEST_INFERREQUESTEDOUTPUTTENSOR,
               '__module__': 'grpc_service_pb2'
            }),
            'ParametersEntry': _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
                'DESCRIPTOR': _MODELINFERREQUEST_PARAMETERSENTRY,
                '__module__': 'grpc_service_pb2'
            }),
            'DESCRIPTOR': _MODELINFERREQUEST,
            '__module__': 'grpc_service_pb2'
        })
        # respose config
        self.ModelInferResponse = _reflection.GeneratedProtocolMessageType('ModelInferResponse', (_message.Message,), {
            'InferOutputTensor': _reflection.GeneratedProtocolMessageType('InferOutputTensor', (_message.Message,), {
                'ParametersEntry': _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
                    'DESCRIPTOR': _MODELINFERRESPONSE_INFEROUTPUTTENSOR_PARAMETERSENTRY,
                    '__module__': 'grpc_service_pb2'
                }),
                'DESCRIPTOR': _MODELINFERRESPONSE_INFEROUTPUTTENSOR,
                '__module__': 'grpc_service_pb2'
            }),
            'ParametersEntry': _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
                'DESCRIPTOR': _MODELINFERRESPONSE_PARAMETERSENTRY,
                '__module__': 'grpc_service_pb2'
            }),
            'DESCRIPTOR': _MODELINFERRESPONSE,
            '__module__': 'grpc_service_pb2'
        })

    @staticmethod
    def GetConfig():
        if GRPCConfig._instance == None :
            GRPCConfig._instance = GRPCConfig()
        return GRPCConfig._instance

class GRPCInferenceServiceStub(object):
    def __init__(self, channel, gRPCConfig):
        self.ModelInfer = channel.unary_unary(
            '/inference.GRPCInferenceService/ModelInfer',
            request_serializer=gRPCConfig.ModelInferRequest.SerializeToString,
            response_deserializer=gRPCConfig.ModelInferResponse.FromString,
            )

def triton_to_np_dtype(dtype):
    if dtype == "BOOL":
        return bool
    elif dtype == "INT8":
        return np.int8
    elif dtype == "INT16":
        return np.int16
    elif dtype == "INT32":
        return np.int32
    elif dtype == "INT64":
        return np.int64
    elif dtype == "UINT8":
        return np.uint8
    elif dtype == "UINT16":
        return np.uint16
    elif dtype == "UINT32":
        return np.uint32
    elif dtype == "UINT64":
        return np.uint64
    elif dtype == "FP16":
        return np.float16
    elif dtype == "FP32" or dtype == "BF16":
        return np.float32
    elif dtype == "FP64":
        return np.float64
    elif dtype == "BYTES":
        return np.object_
    return None
def np_dtype_to_triton(dtype):
    if dtype == bool :
        return "BOOL"
    elif dtype == np.int8 :
        return "INT8"
    elif dtype == np.int16:
        return "INT16"
    elif dtype == np.int32:
        return "INT32"
    elif dtype == np.int64:
        return "INT64"
    elif dtype == np.uint8:
        return "UINT8"
    elif dtype == np.uint16:
        return "UINT16"
    elif dtype == np.uint32:
        return "UINT32"
    elif dtype == np.uint64:
        return "UINT64"
    elif dtype == np.float16:
        return "FP16"
    elif dtype == np.float32:
        return "FP32"
    elif dtype == np.float64:
        return "FP64"
    elif dtype == np.object_:
        return "BYTES"
    return None

class ProtocolClass(object):

    def __init__(self):
        pass

    def http_send_request(self, img_np_array):
        pass

    def grpc_send_request(self, img_np_array):
        pass

class ProtoTriton(ProtocolClass):
    def __init__(self, config):
        super(ProtoTriton, self).__init__()
        self.model_name = config["model_name"]
        # setup http
        self.dict_http = config['http']
        self.url_http = 'http://'+config['tritonclient_server'] + ':' + config['http'][
            'port'] + '/v2/models/' + self.model_name + '/infer'

        # setup grpc
        self.dict_grpc = config['grpc']
        self.url_grpc = config['tritonclient_server'] + ':' + config['grpc']['port']
        self.grpc_config_options = self.dict_grpc["grpc_config_options"]
        self.signature_name = self.dict_grpc["signature_name"]

    def http_send_request(self, request_config):
        if self.dict_http is None:
            return "HTTP's protocol is not setting."

        # input infomation
        inputs = []
        binary_data_arr = None
        for input in request_config['inputs']:
            binary_data = input['data'].tobytes()
            print(input['data'].dtype)
            inputs.append({
                'name': input['name'],  # input name
                'shape': input['data'].shape,  # input shape
                'datatype': np_dtype_to_triton(input['data'].dtype),  # data type
                'parameters': {'binary_data_size': len(binary_data)}
            })
            if binary_data_arr == None:
                binary_data_arr = binary_data
            else:
                binary_data_arr = struct.pack('{}s{}s'.format(len(binary_data_arr), len(binary_data)), binary_data_arr, binary_data)

        outputs = []
        for output in request_config['outputs']:
            outputs.append({
                'name': output['name'],  # output name
                'parameters': {'binary_data': True}
            })

        # data config
        data = json.dumps({
            'id': '1',  # Optional id request
            'inputs': inputs,
            'outputs': outputs,
            'parameters':
                {
                    'sequence_id': 0,  # 0 - not belong to a sequence
                    'sequence_start': False,  # False - first object of the sequence
                    'sequence_end': False,  # False - last object of the sequence
                    'priority': 0,  # 0 - lower value priorities indicate higher priority levels
                    'timeout': 0,  # 0 - the timeout value for the request (microseconds)
                }
        })

        # request body
        request_body = struct.pack('{}s{}s'.format(len(data), len(binary_data_arr)), data.encode(), binary_data_arr)

        # header
        headers = {
            'Content-Type': 'application/json',
            "Inference-Header-Content-Length": str(len(data))
        }

        json_response = requests.post(
            self.url_http,
            data=request_body,
            headers=headers
        )

        if json_response.status_code == 200:
            # binary_data_size
            binary_data_sizes = list(map(int, re.findall(r"(?<={\"binary_data_size\":)[\d]*(?=})", json_response.text)))

            # get json and binary data
            struct_format = ''
            total_binary_len = 0
            for binary_data_size in binary_data_sizes:
                struct_format += str(binary_data_size) + 's'
                total_binary_len += binary_data_size
            struct_format = str(len(json_response.content) - total_binary_len) + 's' + struct_format
            unpacked_content = struct.unpack(struct_format, json_response.content)
            response_body = unpacked_content[0]
            binary_outputs = unpacked_content[1:]

            # parse json
            json_response = json.loads(response_body)

            # parse output
            outputs = []
            for binary_output, json_output in zip(binary_outputs, json_response['outputs']):
                triton_types = json_output['datatype']
                dtype = triton_to_np_dtype(triton_types)
                shape = json_output['shape']
                data = np.frombuffer(binary_output, dtype).reshape(shape)
                outputs.append({
                    'name' : json_output['name'],
                    'dtype': dtype,
                    'shape': shape,
                    'data' : data
                })
            return outputs
        else:
            return None

    def grpc_send_request(self, request_config):
        if self.dict_grpc is None:
            return "gRPC's protocol is not setting."

        # create GRPCConfig
        gRPCConfig = GRPCConfig.GetConfig()
        # Create gRPC stub for communicating with the server
        channel = grpc.insecure_channel(self.url_grpc)
        grpc_stub = GRPCInferenceServiceStub(channel, gRPCConfig)

        # Infer request
        request = gRPCConfig.ModelInferRequest()
        request.model_name = self.model_name
        request.model_version = '1' #self.model_version
        request.id = ""

        # input
        inputs =[]
        binary_data_arr = []
        for input_cfg in request_config['inputs']:
            binary_data = input_cfg['data'].tobytes()
            input = gRPCConfig.ModelInferRequest().InferInputTensor()
            input.name = input_cfg['name']  # input name
            input.datatype = np_dtype_to_triton(input_cfg['data'].dtype)  # data type
            input.shape.extend(input_cfg['data'].shape)  # input shape
            inputs.append(input)
            binary_data_arr.append(binary_data)
            pass
        request.inputs.extend(inputs)
        request.raw_input_contents.extend(binary_data_arr)
        # output
        outputs = []
        for output_cfg in request_config['outputs']:
            output = gRPCConfig.ModelInferRequest().InferRequestedOutputTensor()
            output.name = output_cfg['name']  # input name
            outputs.append(output)
            pass
        request.outputs.extend(outputs)

        # infer
        response = grpc_stub.ModelInfer(request)

        # get json and binary data
        outputs = []
        for i, output in enumerate(response.outputs):
            dtype = triton_to_np_dtype(output.datatype)
            data = list(response.raw_output_contents)[i]
            data = np.frombuffer(data, dtype).reshape(output.shape)
            outputs.append({
                'name': output.name,
                'dtype': dtype,
                'shape': output.shape,
                'data': data
            })
        return outputs








#================ test =======================

proto_config = {
    'model_name': 'imagenet_mobilenetv3',
    'tritonclient_server':'172.16.1.197',
    'http': {
        'port':'30000',
    },
    'grpc': {
        'port': '30001',
        'grpc_config_options': None,
        'signature_name': None
    }
}

p = ProtoTriton(proto_config)


import numpy as np
import PIL.Image

a = PIL.Image.open(r'C:\Users\hien-dv\Downloads\Bengal_tiger_(Panthera_tigris_tigris)_female_3_crop.jpg')
a = np.array(a.resize((224,224), resample=0), dtype=np.float32)
a = a/255.
a = a.reshape((-1,224,224,3))
# print(a)

# request
request_config = {
    'inputs':
    [
        {
            'name': 'inputs',
            'data': a
        }
    ],
    'outputs':
    [
        {'name': 'logits'},
    ]
}

q = p.grpc_send_request(request_config)
# q = p.http_send_request(request_config)
# response
# [
#     {
#         'name': 'model_2',
#         'dtype': <class 'numpy.float32'>,
#         'shape': [1, 5972, 4],
#         'data': np.array()
#     },...
# ]


print(q)

import tensorflow as tf
probabilities = tf.nn.softmax(q[0]['data']).numpy()
top_5 = tf.argsort(probabilities, axis=-1, direction="DESCENDING")[0][:5].numpy()
print(top_5)
