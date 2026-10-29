# MCP server

Serveur local prÃ©vu, de prÃ©fÃ©rence en transport stdio. Il doit appeler `core/` sans dupliquer la logique mÃ©tier.
Outils envisagÃ©s : `brain_search`, `brain_read`, `brain_get_related`, `brain_check_duplicates`, `brain_propose_change`, `brain_apply_change`, `brain_status`, `brain_reindex`.
Aucun outil gÃ©nÃ©rique d'exÃ©cution shell/SQL ou d'Ã©criture arbitraire de fichier.
