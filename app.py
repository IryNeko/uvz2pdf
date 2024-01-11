'''
Gradio app
'''
import gradio
import main

with gradio.Blocks() as demo:
    with gradio.Row():
        upload=gradio.File(label="upload",file_types=['.uvz'])
        convert=gradio.Button(value="等待文件\nwaiting for upload",interactive=False)
        download=gradio.File(label="download")
    @upload.change(outputs=convert)
    def _upload():
        return gradio.Button(value="进行转化\nconvert to pdf",interactive=True)
    @convert.click(inputs=upload,outputs=download)
    def _convert(path):
        main.uvz_unzip(path)
        p=main.dpg_to_pdf(path)
        main.cleanup()
        return p
        
if __name__=="__main__":
    demo.launch()