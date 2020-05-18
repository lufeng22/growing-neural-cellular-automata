import cv2
import torch as t

from lib.model import input
from lib.model.cell_growth_model import CellGrowthModel
from lib.util import img
from lib.util.config import Config
from lib.util.logger_factory import LoggerFactory

if __name__ == "__main__":
    cfg = Config('config.yaml')
    LoggerFactory(cfg['logger']).create()

    model = CellGrowthModel.create(cfg)

    input_tensor = input.from_img('data/dragon.png', in_channels=cfg['model.in-channels'])
    input_batch = t.stack([input_tensor.clone()], 0)

    img.show(input_tensor, size=(1500, 1500))
    output = input_batch
    for index in range(0, 120):
        output = model.forward(output)

        img.show(
            output[0],
            title=f'Step: {index}',
            size=(1500, 1500)
        )

    cv2.destroyAllWindows()
