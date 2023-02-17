import type { PageServerLoad } from './$types';
import { getStudies } from "$helper/sqlHelper";

export const load = (() => {
    const studies = getStudies();

    return {studies};
}) satisfies PageServerLoad;