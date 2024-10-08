"use client";

import { useEffect } from 'react';

export default function ImportBootstrap() {
    useEffect(() => {
        import('bootstrap');
    }, []);

    return null;
}