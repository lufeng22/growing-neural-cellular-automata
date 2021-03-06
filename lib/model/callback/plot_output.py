from lib.model.callback.callback import Callback
from lib.util import img
import torch as t


class PlotOutput(Callback):
    def __init__(self, target, init=10, every=1, window_size=(500, 500), close_key=None):
        self.__target = target
        self.__init = init
        self.__every = every
        self.__window_size = window_size
        self.__close_key = close_key

    def perform(self, ctx):
        if ctx.epoch >= self.__init and ctx.epoch % self.__every == 0:
            current = ctx.output_batch[0][0:4, :]
            if self.__target is None:
                image = current
            else:
                image = t.cat((current, self.__target[0:4, :, :]), 2)

            img.show_tensor(
                image,
                title=f'Epoch {ctx.epoch}/{ctx.epochs}',
                size=self.__window_size,
                close_key=self.__close_key
            )
