interface NavButton {
    text: string; 
    href?: string;
    action?: () => void;
}

export type NavButtons = NavButton[];