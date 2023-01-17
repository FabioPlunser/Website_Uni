interface Nav {
    text: string; 
    href?: string;
    icon?: string;
    children?: Nav[];
}

export type NavButtons = NavButton[];