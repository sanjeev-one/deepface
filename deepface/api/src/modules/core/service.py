from deepface import DeepFace

# pylint: disable=broad-except


def represent(img_path, model_name, detector_backend, enforce_detection, align):
    try:
        result = {}
        embedding_objs = DeepFace.represent(
            img_path=img_path,
            model_name=model_name,
            detector_backend=detector_backend,
            enforce_detection=enforce_detection,
            align=align,
        )
        result["results"] = embedding_objs
        return result
    except Exception as err:
        return {"error": f"Exception while representing: {str(err)}"}, 400


def verify(
    img1_path, img2_path, model_name, detector_backend, distance_metric, enforce_detection, align
):
    try:
        obj = DeepFace.verify(
            img1_path=img1_path,
            img2_path=img2_path,
            model_name=model_name,
            detector_backend=detector_backend,
            distance_metric=distance_metric,
            align=align,
            enforce_detection=enforce_detection,
        )
        return obj
    except Exception as err:
        return {"error": f"Exception while verifying: {str(err)}"}, 400


def analyze(img_path, actions, detector_backend, enforce_detection, align):
    try:
        result = {}
        demographies = DeepFace.analyze(
            img_path=img_path,
            actions=actions,
            detector_backend=detector_backend,
            enforce_detection=enforce_detection,
            align=align,
            silent=True,
        )
        result["results"] = demographies
        return result
    except Exception as err:
        return {"error": f"Exception while analyzing: {str(err)}"}, 400


def find(
    img_path: str,
    db_path: str,
    model_name: str = "VGG-Face",
    distance_metric: str = "cosine",
    enforce_detection: bool = True,
    detector_backend: str = "opencv",
    align: bool = True,
    expand_percentage: int = 0,
    
    normalization: str = "base",
    silent: bool = False,
):
    """
    Wrapper function to call DeepFace.find with the provided arguments.
    """
    try:
        results = DeepFace.find(
            img_path=img_path,
            db_path=db_path,
            model_name=model_name,
            distance_metric=distance_metric,
            enforce_detection=enforce_detection,
            detector_backend=detector_backend,
            align=align,
            expand_percentage=expand_percentage,
            
            normalization=normalization,
            silent=silent,
        )
        return results
    except Exception as err:
        return {"error": f"Exception while finding: {str(err)}"}, 400