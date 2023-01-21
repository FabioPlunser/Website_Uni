import {toast} from '$stores/toastStore'

export function addToast(message='', theme='alert-info') {
    toast.push(message, {theme: theme})
}

export function addToastByRes(res:Response=null) {
    if(res.success) {
        addToast(res.message, 'alert-success')
    }
    else {
        addToast(res.message, 'alert-error')
    }
}

