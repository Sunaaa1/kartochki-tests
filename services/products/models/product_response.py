from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import StrEnum
from typing import Optional, Union


class ProductStatusEnum(StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class ProductResponse(BaseModel):
    id: str
    orgId: str
    imageUrl: str
    imageStoragePath: Optional[str] = None
    processedImageUrl: Optional[str] = None
    processedImageStoragePath: Optional[str] = None
    status: ProductStatusEnum
    marketplace: str
    brandId: Optional[str] = None
    seoTitle: Optional[str] = None
    description: Optional[str] = None
    attributes: Optional[dict] = None
    categoryId: Optional[str] = None
    keywords: list = []
    bulletPoints: Optional[Union[list, str]] = None
    marketplaceData: Optional[dict] = None
    customPrompt: Optional[str] = None
    errorMessage: Optional[str] = None
    additionalImages: list = []
    bgRemovedImages: list = []
    exportedAt: Optional[datetime] = None
    exportedTo: Optional[str] = None
    isExported: bool
    wbSyncStatus: str
    wbNomenclatureId: Optional[str] = None
    wbPublishedAt: Optional[datetime] = None
    wbSyncError: Optional[str] = None
    createdAt: datetime
    updatedAt: datetime