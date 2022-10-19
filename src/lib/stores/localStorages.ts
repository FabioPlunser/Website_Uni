import { browser } from "$app/environment";


function setSelectedFacultyInLocalStorage(value: any) {
    if(browser){
        localStorage.setItem("selectedFaculty", value);
    }
}

function getSelectedFacultyFromLocalStorage() {
    if(browser){
        return localStorage.getItem("selectedFaculty");
    }
}

function setSelectedCurriculumInLocalStorage(value: any) {
    if(browser){
        localStorage.setItem("selectedFaculty", value);
    }
}

function getSelectedCurriculumInLocalStorage() {
    if(browser){
        return localStorage.getItem("selectedFaculty");
    }
}

function setSelectedCourseTypeInLocalStorage(value: any) {
    if(browser){
        localStorage.setItem("selectedFaculty", value);
    }
}

function getSelectedCourseTypeInLocalStorage() {
    if(browser){
        return localStorage.getItem("selectedFaculty");
    }
}