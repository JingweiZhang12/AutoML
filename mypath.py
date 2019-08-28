class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'pascal':
            return '/home/zhangjw/Datasets/VOCdevkit/VOC2012/'  # folder that contains VOCdevkit/.
        elif dataset == 'sbd':
            return '/homw/zhangjw/Datasets/benchmark_RELEASE/'  # folder that contains dataset/.
        elif dataset == 'cityscapes':
            return '/home/zhangjw/Datasets/cityscapes/'     # foler that contains leftImg8bit/
        elif dataset == 'kd':
            return '/home/zhangjw/Datasets/cityscapes/'
        elif dataset == 'coco':
            return '/home/zhangjw/Datasets/coco2017'
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError
