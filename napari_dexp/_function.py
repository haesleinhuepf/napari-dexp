import napari
from napari_tools_menu import register_function
from napari_time_slicer import time_slicer
from napari_plugin_engine import napari_hook_implementation


@napari_hook_implementation
def napari_experimental_provide_function():
    return [denoise_butterworth_napari]


@register_function(menu="Filtering / noise removal > Butterworth (dexp)")
@time_slicer
def denoise_butterworth_napari(
    image: napari.types.ImageData,
    freq_cutoff: float = 0.5,
    order: float = 1,
    padding: int = 32,
    viewer:napari.Viewer = None) -> napari.types.ImageData:

    from dexp.processing.denoising import denoise_butterworth

    return denoise_butterworth(image=image,
                               freq_cutoff=freq_cutoff,
                               order=order,
                               padding=padding)


@register_function(menu="Filtering / deconvolution > Lucy-Richardson (dexp)")
@time_slicer
def lucy_richardson_deconvolution_napari(
    image: napari.types.ImageData,
    psf: napari.types.ImageData,
    num_iterations: int = 10) -> napari.types.ImageData:

    from dexp.processing.deconvolution import lucy_richardson_deconvolution

    return lucy_richardson_deconvolution(
        image=image,
        psf=psf,
        num_iterations=num_iterations
    )

@register_function(menu="Filtering / edge enhancement > Sobel (dexp)")
@time_slicer
def sobel_filter_napari(
    image: napari.types.ImageData,
    exponent: int = 2,
    gamma: float = 1) -> napari.types.ImageData:

    from dexp.processing.filters.sobel_filter import sobel_filter

    return sobel_filter(
        image=image,
        exponent=exponent,
        gamma=gamma)