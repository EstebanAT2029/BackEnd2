-- CreateTable
CREATE TABLE "archivos" (
    "id" SERIAL NOT NULL,
    "nombre" TEXT NOT NULL,
    "extension" TEXT NOT NULL,
    "folder" TEXT NOT NULL,
    "productoid" INTEGER,

    CONSTRAINT "archivos_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "archivos" ADD CONSTRAINT "archivos_productoid_fkey" FOREIGN KEY ("productoid") REFERENCES "productos"("id") ON DELETE SET NULL ON UPDATE CASCADE;
